"""
Portfolio backtesting engine.
Handles portfolio construction, rebalancing, and performance calculation.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from dataclasses import dataclass

from .config import INITIAL_CAPITAL, RISK_FREE_RATE


@dataclass
class PortfolioMetrics:
    """Container for portfolio performance metrics."""
    initial_capital: float
    final_value: float
    total_return: float
    total_return_pct: float
    annualized_return: float
    annualized_volatility: float
    sharpe_ratio: float
    sortino_ratio: float
    max_drawdown: float
    calmar_ratio: float
    win_rate: float
    var_95: float
    num_assets: int


class BacktestEngine:
    """
    Portfolio backtesting engine with performance metrics calculation.
    """
    
    def __init__(self, initial_capital: float = INITIAL_CAPITAL):
        """
        Initialize backtesting engine.
        
        Args:
            initial_capital: Starting capital for backtesting
        """
        self.initial_capital = initial_capital
        self.portfolio_values = {}
        self.portfolio_returns = {}
        self.portfolio_metrics = {}
        
    def backtest_portfolio(
        self,
        portfolio_name: str,
        weights: Dict[str, float],
        price_data: pd.DataFrame
    ) -> Tuple[pd.Series, pd.Series]:
        """
        Backtest a single portfolio with given weights.
        
        Args:
            portfolio_name: Name of the portfolio
            weights: Dictionary of asset weights {asset_code: weight}
            price_data: DataFrame with asset prices (index=Date, columns=asset_codes)
            
        Returns:
            Tuple of (portfolio_values, portfolio_returns)
        """
        # Validate weights
        total_weight = sum(weights.values())
        if not np.isclose(total_weight, 1.0, atol=1e-6):
            raise ValueError(f"Portfolio weights must sum to 1.0, got {total_weight}")
        
        # Filter price data to only include assets in portfolio
        available_assets = [asset for asset in weights.keys() if asset in price_data.columns]
        if len(available_assets) != len(weights):
            missing = set(weights.keys()) - set(available_assets)
            raise ValueError(f"Missing assets in price data: {missing}")
        
        # Calculate portfolio returns
        returns = price_data[available_assets].pct_change()
        
        # Weight the returns
        weighted_returns = pd.Series(0.0, index=returns.index)
        for asset, weight in weights.items():
            if asset in available_assets:
                weighted_returns += returns[asset] * weight
        
        # Calculate portfolio value over time
        portfolio_values = pd.Series(self.initial_capital, index=returns.index)
        for i in range(1, len(portfolio_values)):
            portfolio_values.iloc[i] = portfolio_values.iloc[i-1] * (1 + weighted_returns.iloc[i])
        
        # Store results
        self.portfolio_values[portfolio_name] = portfolio_values
        self.portfolio_returns[portfolio_name] = weighted_returns
        
        return portfolio_values, weighted_returns
    
    def calculate_metrics(
        self,
        portfolio_name: str,
        num_assets: int = None
    ) -> PortfolioMetrics:
        """
        Calculate performance metrics for a portfolio.
        
        Args:
            portfolio_name: Name of the portfolio
            num_assets: Number of assets in portfolio (optional)
            
        Returns:
            PortfolioMetrics object with all calculated metrics
        """
        if portfolio_name not in self.portfolio_values:
            raise ValueError(f"Portfolio '{portfolio_name}' not found. Run backtest first.")
        
        values = self.portfolio_values[portfolio_name]
        returns = self.portfolio_returns[portfolio_name]
        
        # Basic metrics
        final_value = values.iloc[-1]
        total_return = final_value - self.initial_capital
        total_return_pct = (final_value / self.initial_capital - 1) * 100
        
        # Annualized metrics
        num_days = len(returns)
        years = num_days / 252
        annualized_return = (final_value / self.initial_capital) ** (1 / years) - 1
        annualized_volatility = returns.std() * np.sqrt(252)
        
        # Risk-adjusted metrics
        excess_return = annualized_return - RISK_FREE_RATE
        sharpe_ratio = excess_return / annualized_volatility if annualized_volatility > 0 else 0
        
        # Sortino ratio (downside deviation)
        downside_returns = returns[returns < 0]
        downside_std = downside_returns.std() * np.sqrt(252)
        sortino_ratio = excess_return / downside_std if downside_std > 0 else 0
        
        # Maximum drawdown
        cumulative = (1 + returns).cumprod()
        running_max = cumulative.expanding().max()
        drawdown = (cumulative - running_max) / running_max
        max_drawdown = drawdown.min()
        
        # Calmar ratio
        calmar_ratio = annualized_return / abs(max_drawdown) if max_drawdown != 0 else 0
        
        # Win rate
        win_rate = (returns > 0).sum() / len(returns) * 100
        
        # Value at Risk (95% confidence)
        var_95 = returns.quantile(0.05)
        
        # Create metrics object
        metrics = PortfolioMetrics(
            initial_capital=self.initial_capital,
            final_value=final_value,
            total_return=total_return,
            total_return_pct=total_return_pct,
            annualized_return=annualized_return * 100,  # Convert to percentage
            annualized_volatility=annualized_volatility * 100,
            sharpe_ratio=sharpe_ratio,
            sortino_ratio=sortino_ratio,
            max_drawdown=max_drawdown * 100,
            calmar_ratio=calmar_ratio,
            win_rate=win_rate,
            var_95=var_95 * 100,
            num_assets=num_assets or 0
        )
        
        self.portfolio_metrics[portfolio_name] = metrics
        return metrics
    
    def backtest_all_portfolios(
        self,
        portfolios: Dict[str, Dict[str, float]],
        price_data: pd.DataFrame
    ) -> Dict[str, PortfolioMetrics]:
        """
        Backtest multiple portfolios.
        
        Args:
            portfolios: Dictionary of {portfolio_name: {asset: weight}}
            price_data: DataFrame with asset prices
            
        Returns:
            Dictionary of {portfolio_name: PortfolioMetrics}
        """
        print("\n" + "="*80)
        print("BACKTESTING PORTFOLIOS")
        print("="*80)
        
        results = {}
        
        for portfolio_name, weights in portfolios.items():
            try:
                # Run backtest
                values, returns = self.backtest_portfolio(
                    portfolio_name, weights, price_data
                )
                
                # Calculate metrics
                metrics = self.calculate_metrics(
                    portfolio_name,
                    num_assets=len(weights)
                )
                
                results[portfolio_name] = metrics
                
                print(f"✓ {portfolio_name:30s}: "
                      f"Return={metrics.total_return_pct:6.2f}%, "
                      f"Sharpe={metrics.sharpe_ratio:5.2f}")
                
            except Exception as e:
                print(f"✗ {portfolio_name:30s}: Error - {str(e)}")
        
        print(f"\n✓ Successfully backtested {len(results)}/{len(portfolios)} portfolios")
        return results
    
    def get_summary_dataframe(self) -> pd.DataFrame:
        """
        Get summary DataFrame of all portfolio metrics.
        
        Returns:
            DataFrame with portfolios as rows and metrics as columns
        """
        if not self.portfolio_metrics:
            raise ValueError("No portfolios backtested yet.")
        
        data = []
        for name, metrics in self.portfolio_metrics.items():
            data.append({
                'Portfolio': name,
                'Initial Capital': f"{metrics.initial_capital:,.0f}",
                'Final Value': f"{metrics.final_value:,.2f}",
                'Total Return': f"{metrics.total_return:,.2f}",
                'Total Return %': f"{metrics.total_return_pct:.2f}%",
                'Annualized Return': f"{metrics.annualized_return:.2f}%",
                'Annualized Volatility': f"{metrics.annualized_volatility:.2f}%",
                'Sharpe Ratio': f"{metrics.sharpe_ratio:.2f}",
                'Sortino Ratio': f"{metrics.sortino_ratio:.2f}",
                'Max Drawdown': f"{metrics.max_drawdown:.2f}%",
                'Calmar Ratio': f"{metrics.calmar_ratio:.2f}",
                'Win Rate': f"{metrics.win_rate:.2f}%",
                'VaR 95%': f"{metrics.var_95:.2f}%",
                'Num Assets': metrics.num_assets,
            })
        
        df = pd.DataFrame(data)
        
        # Sort by Sharpe Ratio (descending)
        df['_sharpe_sort'] = df['Sharpe Ratio'].str.replace('', '0').astype(float)
        df = df.sort_values('_sharpe_sort', ascending=False).drop('_sharpe_sort', axis=1)
        
        return df
    
    def get_drawdown_series(self, portfolio_name: str) -> pd.Series:
        """
        Calculate drawdown series for a portfolio.
        
        Args:
            portfolio_name: Name of the portfolio
            
        Returns:
            Series of drawdown values over time
        """
        if portfolio_name not in self.portfolio_returns:
            raise ValueError(f"Portfolio '{portfolio_name}' not found.")
        
        returns = self.portfolio_returns[portfolio_name]
        cumulative = (1 + returns).cumprod()
        running_max = cumulative.expanding().max()
        drawdown = (cumulative - running_max) / running_max
        
        return drawdown * 100  # Convert to percentage
    
    def get_rolling_sharpe(
        self,
        portfolio_name: str,
        window: int = 60
    ) -> pd.Series:
        """
        Calculate rolling Sharpe ratio for a portfolio.
        
        Args:
            portfolio_name: Name of the portfolio
            window: Rolling window size in days
            
        Returns:
            Series of rolling Sharpe ratios
        """
        if portfolio_name not in self.portfolio_returns:
            raise ValueError(f"Portfolio '{portfolio_name}' not found.")
        
        returns = self.portfolio_returns[portfolio_name]
        
        # Rolling mean and std
        rolling_mean = returns.rolling(window).mean() * 252
        rolling_std = returns.rolling(window).std() * np.sqrt(252)
        
        # Rolling Sharpe
        rolling_sharpe = (rolling_mean - RISK_FREE_RATE) / rolling_std
        
        return rolling_sharpe
