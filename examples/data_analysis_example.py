"""
Example: Analyzing asset data and correlations.

This example demonstrates how to:
1. Load and explore asset data
2. Calculate correlations
3. Generate statistics
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data_loader import DataLoader
import pandas as pd


def main():
    """Analyze asset data."""
    
    print("\n" + "="*80)
    print("ASSET DATA ANALYSIS")
    print("="*80)
    
    # Load data
    print("\nLoading asset data...")
    loader = DataLoader()
    loader.load_all_assets()
    loader.align_data()
    
    # Display summary
    loader.summary()
    
    # Get correlation matrix
    print("\n" + "-"*80)
    print("CORRELATION MATRIX")
    print("-"*80)
    corr = loader.get_correlation_matrix()
    print(corr.round(2))
    
    # Find highly correlated pairs
    print("\n" + "-"*80)
    print("HIGHLY CORRELATED ASSET PAIRS (>0.7)")
    print("-"*80)
    
    for i in range(len(corr.columns)):
        for j in range(i+1, len(corr.columns)):
            if corr.iloc[i, j] > 0.7:
                print(f"{corr.columns[i]:15s} <-> {corr.columns[j]:15s}: {corr.iloc[i, j]:.3f}")
    
    # Get asset statistics
    print("\n" + "-"*80)
    print("ASSET STATISTICS")
    print("-"*80)
    stats = loader.get_asset_statistics()
    print(stats.round(4))
    
    # Find best and worst performers
    print("\n" + "-"*80)
    print("PERFORMANCE RANKING")
    print("-"*80)
    
    ranked = stats.sort_values('Annualized Return', ascending=False)
    print("\nTop 5 Performers:")
    for idx, (asset, row) in enumerate(ranked.head(5).iterrows(), 1):
        print(f"{idx}. {asset:15s}: {row['Annualized Return']*100:6.2f}% "
              f"(Vol: {row['Annualized Volatility']*100:5.2f}%)")
    
    print("\nBottom 5 Performers:")
    for idx, (asset, row) in enumerate(ranked.tail(5).iterrows(), 1):
        print(f"{idx}. {asset:15s}: {row['Annualized Return']*100:6.2f}% "
              f"(Vol: {row['Annualized Volatility']*100:5.2f}%)")
    
    print("\n" + "="*80 + "\n")


if __name__ == '__main__':
    main()
