"""
Visualization module for portfolio analysis.
Generates comprehensive charts and plots for portfolio performance analysis.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Dict, List, Optional

from .config import (
    VISUALIZATION_DIR, COLOR_PALETTE, CHART_COLORS,
    MATPLOTLIB_STYLE
)


class PortfolioVisualizer:
    """
    Creates visualizations for portfolio analysis results.
    """
    
    def __init__(self, output_dir: Path = VISUALIZATION_DIR):
        """
        Initialize visualizer.
        
        Args:
            output_dir: Directory to save visualization outputs
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self._setup_style()
        
    def _setup_style(self):
        """Configure matplotlib style settings."""
        plt.rcParams.update(MATPLOTLIB_STYLE)
        sns.set_palette(CHART_COLORS)
        
    def plot_correlation_heatmap(
        self,
        correlation_matrix: pd.DataFrame,
        filename: str = '01_correlation_heatmap.png'
    ):
        """
        Plot correlation heatmap of asset returns.
        
        Args:
            correlation_matrix: Correlation matrix DataFrame
            filename: Output filename
        """
        fig, ax = plt.subplots(figsize=(16, 14))
        
        # Create heatmap
        sns.heatmap(
            correlation_matrix,
            annot=True,
            fmt='.2f',
            cmap='RdYlGn',
            center=0,
            square=True,
            linewidths=0.5,
            cbar_kws={'label': 'Correlation Coefficient'},
            ax=ax
        )
        
        ax.set_title('Asset Correlation Matrix', fontsize=22, fontweight='bold', pad=20)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Saved: {filename}")
        
    def plot_portfolio_values(
        self,
        portfolio_values: Dict[str, pd.Series],
        filename: str = '02_portfolio_values.png'
    ):
        """
        Plot portfolio value curves over time.
        
        Args:
            portfolio_values: Dictionary of {portfolio_name: value_series}
            filename: Output filename
        """
        fig, ax = plt.subplots(figsize=(18, 10))
        
        colors = CHART_COLORS
        
        for idx, (name, values) in enumerate(portfolio_values.items()):
            ax.plot(
                values.index,
                values.values,
                label=name,
                linewidth=2.5,
                color=colors[idx % len(colors)],
                alpha=0.9
            )
        
        ax.set_xlabel('Date', fontsize=14, fontweight='bold')
        ax.set_ylabel('Portfolio Value (CNY)', fontsize=14, fontweight='bold')
        ax.set_title('Portfolio Net Asset Value Over Time', fontsize=22, fontweight='bold', pad=20)
        
        ax.legend(loc='best', fontsize=11, framealpha=0.95)
        ax.grid(True, alpha=0.3)
        
        # Format y-axis with comma separators
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Saved: {filename}")
        
    def plot_drawdown_curves(
        self,
        drawdown_series: Dict[str, pd.Series],
        filename: str = '03_drawdown_curves.png'
    ):
        """
        Plot drawdown curves for portfolios.
        
        Args:
            drawdown_series: Dictionary of {portfolio_name: drawdown_series}
            filename: Output filename
        """
        fig, ax = plt.subplots(figsize=(18, 10))
        
        colors = CHART_COLORS
        
        for idx, (name, drawdown) in enumerate(drawdown_series.items()):
            ax.fill_between(
                drawdown.index,
                0,
                drawdown.values,
                alpha=0.3,
                color=colors[idx % len(colors)],
                label=name
            )
            ax.plot(
                drawdown.index,
                drawdown.values,
                linewidth=2,
                color=colors[idx % len(colors)],
                alpha=0.9
            )
        
        ax.set_xlabel('Date', fontsize=14, fontweight='bold')
        ax.set_ylabel('Drawdown (%)', fontsize=14, fontweight='bold')
        ax.set_title('Portfolio Drawdown Analysis', fontsize=22, fontweight='bold', pad=20)
        
        ax.legend(loc='lower right', fontsize=11, framealpha=0.95)
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Saved: {filename}")
        
    def plot_cumulative_returns(
        self,
        returns_dict: Dict[str, pd.Series],
        filename: str = '04_cumulative_returns.png'
    ):
        """
        Plot cumulative returns for portfolios.
        
        Args:
            returns_dict: Dictionary of {portfolio_name: returns_series}
            filename: Output filename
        """
        fig, ax = plt.subplots(figsize=(18, 10))
        
        colors = CHART_COLORS
        
        for idx, (name, returns) in enumerate(returns_dict.items()):
            cumulative = (1 + returns).cumprod() - 1
            ax.plot(
                cumulative.index,
                cumulative.values * 100,
                label=name,
                linewidth=2.5,
                color=colors[idx % len(colors)],
                alpha=0.9
            )
        
        ax.set_xlabel('Date', fontsize=14, fontweight='bold')
        ax.set_ylabel('Cumulative Return (%)', fontsize=14, fontweight='bold')
        ax.set_title('Portfolio Cumulative Returns', fontsize=22, fontweight='bold', pad=20)
        
        ax.legend(loc='best', fontsize=11, framealpha=0.95)
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='black', linestyle='--', linewidth=0.8)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Saved: {filename}")
        
    def plot_efficient_frontier(
        self,
        metrics_dict: Dict[str, tuple],
        filename: str = '05_efficient_frontier.png'
    ):
        """
        Plot efficient frontier with portfolio positions.
        
        Args:
            metrics_dict: Dictionary of {portfolio_name: (volatility, return)}
            filename: Output filename
        """
        fig, ax = plt.subplots(figsize=(16, 10))
        
        colors = CHART_COLORS
        legend_handles = []
        
        for idx, (name, (vol, ret)) in enumerate(metrics_dict.items()):
            # Plot portfolio point
            ax.scatter(
                vol, ret,
                s=2000,
                color=colors[idx % len(colors)],
                edgecolors='black',
                linewidth=4,
                zorder=5,
                marker='D',
                alpha=0.9
            )
            
            # Create legend handle with small square
            legend_handles.append(
                plt.Line2D(
                    [0], [0],
                    marker='s',
                    color='w',
                    markerfacecolor=colors[idx % len(colors)],
                    markersize=10,
                    label=name,
                    markeredgecolor='black',
                    markeredgewidth=1.5
                )
            )
        
        ax.set_xlabel('Annualized Volatility (%)', fontsize=15, fontweight='bold')
        ax.set_ylabel('Annualized Return (%)', fontsize=15, fontweight='bold')
        ax.set_title('Portfolio Efficient Frontier', fontsize=22, fontweight='bold', pad=20)
        
        ax.legend(
            handles=legend_handles,
            loc='upper right',
            fontsize=11,
            framealpha=0.95,
            title='Portfolios',
            title_fontsize=12,
            ncol=1,
            fancybox=True,
            shadow=True
        )
        
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Saved: {filename}")
        
    def plot_performance_metrics(
        self,
        metrics_df: pd.DataFrame,
        filename: str = '07_performance_metrics.png'
    ):
        """
        Plot bar charts comparing key performance metrics.
        
        Args:
            metrics_df: DataFrame with portfolio metrics
            filename: Output filename
        """
        # Select key metrics to plot
        metrics_to_plot = [
            'Annualized Return',
            'Annualized Volatility',
            'Sharpe Ratio',
            'Max Drawdown'
        ]
        
        fig, axes = plt.subplots(2, 2, figsize=(20, 14))
        axes = axes.flatten()
        
        colors = CHART_COLORS
        
        for idx, metric in enumerate(metrics_to_plot):
            ax = axes[idx]
            
            # Extract values (remove % and convert to float)
            values = metrics_df[metric].str.replace('%', '').astype(float)
            portfolios = metrics_df['Portfolio']
            
            # Create bar chart
            bars = ax.barh(
                portfolios,
                values,
                color=[colors[i % len(colors)] for i in range(len(portfolios))],
                edgecolor='black',
                linewidth=1.5,
                alpha=0.85
            )
            
            ax.set_xlabel(metric, fontsize=13, fontweight='bold')
            ax.set_title(f'{metric} Comparison', fontsize=16, fontweight='bold', pad=15)
            ax.grid(True, alpha=0.3, axis='x')
            
            # Add value labels
            for bar in bars:
                width = bar.get_width()
                ax.text(
                    width,
                    bar.get_y() + bar.get_height()/2,
                    f'{width:.2f}',
                    ha='left' if width >= 0 else 'right',
                    va='center',
                    fontsize=10,
                    fontweight='bold'
                )
        
        plt.suptitle('Portfolio Performance Metrics Comparison', 
                     fontsize=24, fontweight='bold', y=0.995)
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Saved: {filename}")
        
    def plot_portfolio_allocations(
        self,
        portfolios: Dict[str, Dict[str, float]],
        filename: str = '08_portfolio_allocations.png'
    ):
        """
        Plot pie charts showing asset allocation for each portfolio.
        
        Args:
            portfolios: Dictionary of {portfolio_name: {asset: weight}}
            filename: Output filename
        """
        n_portfolios = len(portfolios)
        cols = 3
        rows = (n_portfolios + cols - 1) // cols
        
        fig, axes = plt.subplots(rows, cols, figsize=(20, 6*rows))
        axes = axes.flatten() if n_portfolios > 1 else [axes]
        
        pie_colors = list(COLOR_PALETTE.values())
        
        for idx, (name, weights) in enumerate(portfolios.items()):
            ax = axes[idx]
            
            # Filter out zero weights
            weights_filtered = {k: v for k, v in weights.items() if v > 0.001}
            
            labels = list(weights_filtered.keys())
            sizes = list(weights_filtered.values())
            
            # Create pie chart
            wedges, texts, autotexts = ax.pie(
                sizes,
                labels=labels,
                autopct='%1.1f%%',
                startangle=90,
                colors=pie_colors[:len(labels)],
                textprops={'fontsize': 11, 'fontweight': 'bold'},
                wedgeprops={'edgecolor': 'white', 'linewidth': 2}
            )
            
            ax.set_title(name, fontsize=14, fontweight='bold', pad=15)
        
        # Hide unused subplots
        for idx in range(n_portfolios, len(axes)):
            axes[idx].axis('off')
        
        plt.suptitle('Portfolio Asset Allocations', fontsize=24, fontweight='bold', y=0.995)
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Saved: {filename}")
        
    def plot_returns_distribution(
        self,
        returns_dict: Dict[str, pd.Series],
        filename: str = '09_returns_distribution.png'
    ):
        """
        Plot return distribution histograms for portfolios.
        
        Args:
            returns_dict: Dictionary of {portfolio_name: returns_series}
            filename: Output filename
        """
        n_portfolios = len(returns_dict)
        cols = 3
        rows = (n_portfolios + cols - 1) // cols
        
        fig, axes = plt.subplots(rows, cols, figsize=(20, 6*rows))
        axes = axes.flatten() if n_portfolios > 1 else [axes]
        
        colors = CHART_COLORS
        
        for idx, (name, returns) in enumerate(returns_dict.items()):
            ax = axes[idx]
            
            # Plot histogram
            ax.hist(
                returns.dropna() * 100,
                bins=50,
                color=colors[idx % len(colors)],
                alpha=0.7,
                edgecolor='black',
                linewidth=0.5
            )
            
            # Add vertical line for mean
            mean_return = returns.mean() * 100
            ax.axvline(
                mean_return,
                color='red',
                linestyle='--',
                linewidth=2,
                label=f'Mean: {mean_return:.3f}%'
            )
            
            ax.set_xlabel('Daily Return (%)', fontsize=12, fontweight='bold')
            ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
            ax.set_title(name, fontsize=14, fontweight='bold', pad=10)
            ax.legend(fontsize=10)
            ax.grid(True, alpha=0.3)
        
        # Hide unused subplots
        for idx in range(n_portfolios, len(axes)):
            axes[idx].axis('off')
        
        plt.suptitle('Portfolio Returns Distribution', fontsize=24, fontweight='bold', y=0.995)
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Saved: {filename}")
        
    def plot_rolling_sharpe(
        self,
        rolling_sharpe_dict: Dict[str, pd.Series],
        filename: str = '10_rolling_sharpe.png'
    ):
        """
        Plot rolling Sharpe ratio over time.
        
        Args:
            rolling_sharpe_dict: Dictionary of {portfolio_name: rolling_sharpe_series}
            filename: Output filename
        """
        fig, ax = plt.subplots(figsize=(18, 10))
        
        colors = CHART_COLORS
        
        for idx, (name, sharpe) in enumerate(rolling_sharpe_dict.items()):
            ax.plot(
                sharpe.index,
                sharpe.values,
                label=name,
                linewidth=2.5,
                color=colors[idx % len(colors)],
                alpha=0.9
            )
        
        ax.set_xlabel('Date', fontsize=14, fontweight='bold')
        ax.set_ylabel('Rolling Sharpe Ratio (60-day)', fontsize=14, fontweight='bold')
        ax.set_title('Portfolio Rolling Sharpe Ratio', fontsize=22, fontweight='bold', pad=20)
        
        ax.legend(loc='best', fontsize=11, framealpha=0.95)
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='black', linestyle='--', linewidth=0.8)
        ax.axhline(y=1, color='green', linestyle=':', linewidth=0.8, alpha=0.5)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Saved: {filename}")
        
    def plot_monthly_returns_heatmap(
        self,
        returns: pd.Series,
        portfolio_name: str,
        filename: str = '11_monthly_returns_heatmap.png'
    ):
        """
        Plot monthly returns heatmap for a single portfolio.
        
        Args:
            returns: Daily returns series
            portfolio_name: Name of the portfolio
            filename: Output filename
        """
        # Resample to monthly returns
        monthly_returns = (1 + returns).resample('M').prod() - 1
        
        # Create pivot table (months as rows, years as columns)
        monthly_returns_df = pd.DataFrame({
            'Year': monthly_returns.index.year,
            'Month': monthly_returns.index.month,
            'Return': monthly_returns.values * 100
        })
        
        pivot = monthly_returns_df.pivot(index='Month', columns='Year', values='Return')
        
        # Create heatmap
        fig, ax = plt.subplots(figsize=(12, 8))
        
        sns.heatmap(
            pivot,
            annot=True,
            fmt='.2f',
            cmap='RdYlGn',
            center=0,
            linewidths=0.5,
            cbar_kws={'label': 'Monthly Return (%)'},
            ax=ax
        )
        
        ax.set_title(f'{portfolio_name} - Monthly Returns Heatmap',
                     fontsize=18, fontweight='bold', pad=20)
        ax.set_xlabel('Year', fontsize=14, fontweight='bold')
        ax.set_ylabel('Month', fontsize=14, fontweight='bold')
        
        # Set month labels
        month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        ax.set_yticklabels(month_labels, rotation=0)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Saved: {filename}")
