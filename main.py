"""
Main entry point for Global Asset Portfolio Analysis System.
Run this script to execute the complete portfolio analysis pipeline.
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from src.data_loader import DataLoader
from src.backtest_engine import BacktestEngine
from src.visualizer import PortfolioVisualizer
from src.config import PORTFOLIOS, RESULTS_DIR

import pandas as pd
import warnings
warnings.filterwarnings('ignore')


def main():
    """
    Execute the complete portfolio analysis pipeline.
    """
    print("\n" + "="*80)
    print("GLOBAL ASSET PORTFOLIO ANALYSIS SYSTEM")
    print("="*80)
    
    # ========================================================================
    # STEP 1: Load and prepare data
    # ========================================================================
    print("\n[STEP 1/4] Loading and preparing asset data...")
    
    loader = DataLoader()
    assets_data = loader.load_all_assets()
    
    if len(assets_data) < 5:
        print("\n✗ Error: Insufficient assets loaded. Need at least 5 assets.")
        return
    
    aligned_data, common_dates = loader.align_data()
    loader.summary()
    
    # ========================================================================
    # STEP 2: Backtest portfolios
    # ========================================================================
    print("\n[STEP 2/4] Backtesting portfolios...")
    
    engine = BacktestEngine()
    metrics = engine.backtest_all_portfolios(PORTFOLIOS, aligned_data)
    
    # Save summary to CSV
    summary_df = engine.get_summary_dataframe()
    summary_path = RESULTS_DIR / 'backtest_summary.csv'
    summary_df.to_csv(summary_path, index=False, encoding='utf-8-sig')
    print(f"\n✓ Saved summary to: {summary_path}")
    
    # ========================================================================
    # STEP 3: Generate visualizations
    # ========================================================================
    print("\n[STEP 3/4] Generating visualizations...")
    
    visualizer = PortfolioVisualizer()
    
    # 1. Correlation heatmap
    corr_matrix = loader.get_correlation_matrix()
    visualizer.plot_correlation_heatmap(corr_matrix)
    
    # 2. Portfolio values
    visualizer.plot_portfolio_values(engine.portfolio_values)
    
    # 3. Drawdown curves
    drawdowns = {
        name: engine.get_drawdown_series(name)
        for name in PORTFOLIOS.keys()
    }
    visualizer.plot_drawdown_curves(drawdowns)
    
    # 4. Cumulative returns
    visualizer.plot_cumulative_returns(engine.portfolio_returns)
    
    # 5. Efficient frontier
    efficient_frontier_data = {
        name: (metrics[name].annualized_volatility, metrics[name].annualized_return)
        for name in PORTFOLIOS.keys()
    }
    visualizer.plot_efficient_frontier(efficient_frontier_data)
    
    # 6. Performance metrics
    visualizer.plot_performance_metrics(summary_df)
    
    # 7. Portfolio allocations
    visualizer.plot_portfolio_allocations(PORTFOLIOS)
    
    # 8. Returns distribution
    visualizer.plot_returns_distribution(engine.portfolio_returns)
    
    # 9. Rolling Sharpe ratio
    rolling_sharpe = {
        name: engine.get_rolling_sharpe(name)
        for name in PORTFOLIOS.keys()
    }
    visualizer.plot_rolling_sharpe(rolling_sharpe)
    
    # 10. Monthly returns heatmap (for best portfolio)
    best_portfolio = summary_df.iloc[0]['Portfolio']
    visualizer.plot_monthly_returns_heatmap(
        engine.portfolio_returns[best_portfolio],
        best_portfolio
    )
    
    # ========================================================================
    # STEP 4: Save detailed results
    # ========================================================================
    print("\n[STEP 4/4] Saving detailed results...")
    
    # Save individual portfolio details
    for name in PORTFOLIOS.keys():
        portfolio_df = pd.DataFrame({
            'Date': engine.portfolio_values[name].index,
            'Portfolio Value': engine.portfolio_values[name].values,
            'Daily Return': engine.portfolio_returns[name].values,
            'Cumulative Return': (1 + engine.portfolio_returns[name]).cumprod().values - 1,
        })
        
        # Clean portfolio name for filename
        clean_name = name.replace(' ', '_').replace('/', '_')
        detail_path = RESULTS_DIR / f'{clean_name}_details.csv'
        portfolio_df.to_csv(detail_path, index=False, encoding='utf-8-sig')
    
    print(f"✓ Saved detailed results for {len(PORTFOLIOS)} portfolios")
    
    # ========================================================================
    # Complete
    # ========================================================================
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE!")
    print("="*80)
    print(f"\nResults saved to:")
    print(f"  • Summary: {RESULTS_DIR / 'backtest_summary.csv'}")
    print(f"  • Details: {RESULTS_DIR / '*_details.csv'}")
    print(f"  • Charts:  {visualizer.output_dir / '*.png'}")
    print("\n" + "="*80)
    
    # Print top 3 portfolios
    print("\nTOP 3 PORTFOLIOS (by Sharpe Ratio):")
    print("-" * 80)
    for idx in range(min(3, len(summary_df))):
        row = summary_df.iloc[idx]
        print(f"{idx+1}. {row['Portfolio']}")
        print(f"   Return: {row['Total Return %']:>10s} | "
              f"Sharpe: {row['Sharpe Ratio']:>6s} | "
              f"Max DD: {row['Max Drawdown']:>8s}")
    print("="*80 + "\n")


if __name__ == '__main__':
    main()
