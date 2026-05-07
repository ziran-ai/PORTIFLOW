"""
Example: Creating and backtesting a custom portfolio.

This example demonstrates how to:
1. Define a custom portfolio
2. Load data
3. Run backtest
4. Generate visualizations
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data_loader import DataLoader
from src.backtest_engine import BacktestEngine
from src.visualizer import PortfolioVisualizer
from src.config import RESULTS_DIR, VISUALIZATION_DIR


def main():
    """Run custom portfolio analysis."""
    
    # Define your custom portfolio
    custom_portfolio = {
        'My Tech Portfolio': {
            'NDX': 0.50,   # 50% Nasdaq 100
            'SPX': 0.30,   # 30% S&P 500
            'GLD': 0.20,   # 20% Gold (hedge)
        }
    }
    
    print("\n" + "="*80)
    print("CUSTOM PORTFOLIO ANALYSIS")
    print("="*80)
    
    # Step 1: Load data
    print("\n[1/4] Loading data...")
    loader = DataLoader()
    loader.load_all_assets()
    aligned_data, _ = loader.align_data()
    
    # Step 2: Backtest
    print("\n[2/4] Running backtest...")
    engine = BacktestEngine(initial_capital=1_000_000)
    engine.backtest_all_portfolios(custom_portfolio, aligned_data)
    
    # Step 3: Get results
    print("\n[3/4] Calculating metrics...")
    summary = engine.get_summary_dataframe()
    print("\nResults:")
    print(summary.to_string(index=False))
    
    # Step 4: Visualize
    print("\n[4/4] Generating visualizations...")
    viz = PortfolioVisualizer()
    
    # Portfolio value over time
    viz.plot_portfolio_values(engine.portfolio_values)
    
    # Drawdown analysis
    drawdowns = {
        name: engine.get_drawdown_series(name)
        for name in custom_portfolio.keys()
    }
    viz.plot_drawdown_curves(drawdowns)
    
    # Returns distribution
    viz.plot_returns_distribution(engine.portfolio_returns)
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE!")
    print(f"Results saved to: {RESULTS_DIR}")
    print(f"Charts saved to: {VISUALIZATION_DIR}")
    print("="*80 + "\n")


if __name__ == '__main__':
    main()
