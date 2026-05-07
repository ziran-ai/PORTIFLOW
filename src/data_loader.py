"""
Data loading and preprocessing module.
Handles loading asset price data, cleaning, and alignment.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple
import warnings

from .config import (
    DATA_DIR, ASSET_FILE_MAPPING, ASSET_NAMES,
    START_DATE, END_DATE
)

warnings.filterwarnings('ignore')


class DataLoader:
    """
    Loads and preprocesses asset price data from CSV files.
    """
    
    def __init__(self, data_dir: Path = DATA_DIR):
        """
        Initialize DataLoader.
        
        Args:
            data_dir: Directory containing asset data files
        """
        self.data_dir = Path(data_dir)
        self.assets_data = {}
        self.aligned_data = None
        self.common_dates = None
        
    @staticmethod
    def clean_numeric(value):
        """
        Clean numeric string by removing commas, percent signs, and whitespace.
        
        Args:
            value: String or numeric value to clean
            
        Returns:
            Cleaned string or original value
        """
        if isinstance(value, str):
            return value.replace(',', '').replace('%', '').strip()
        return value
    
    def load_single_asset(self, asset_code: str, filename: str) -> pd.DataFrame:
        """
        Load and preprocess a single asset's data.
        
        Args:
            asset_code: Asset identifier code
            filename: CSV filename
            
        Returns:
            DataFrame with Date and Price columns, or None if loading fails
        """
        filepath = self.data_dir / filename
        
        if not filepath.exists():
            print(f"✗ {asset_code:15s}: File not found - {filename}")
            return None
        
        try:
            # Read CSV file
            df = pd.read_csv(filepath, encoding='utf-8')
            df.columns = df.columns.str.strip().str.replace('"', '')
            
            # Parse date column
            if 'Date' not in df.columns:
                print(f"✗ {asset_code:15s}: No 'Date' column found")
                return None
            
            df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y', errors='coerce')
            
            # Parse price column
            if 'Price' not in df.columns:
                print(f"✗ {asset_code:15s}: No 'Price' column found")
                return None
            
            df['Price'] = df['Price'].apply(self.clean_numeric)
            df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
            
            # Remove null values
            df = df.dropna(subset=['Date', 'Price'])
            
            # Sort by date
            df = df.sort_values('Date').reset_index(drop=True)
            
            # Filter date range
            target_start = pd.Timestamp(START_DATE)
            target_end = pd.Timestamp(END_DATE)
            df = df[(df['Date'] >= target_start) & (df['Date'] <= target_end)].copy()
            
            # Check minimum data points
            if len(df) < 100:
                print(f"✗ {asset_code:15s}: Insufficient data ({len(df)} days)")
                return None
            
            # Remove duplicate dates
            if df['Date'].duplicated().any():
                print(f"  ⚠ {asset_code:15s}: Duplicate dates removed")
                df = df.drop_duplicates(subset=['Date'], keep='first')
            
            # Calculate returns
            df['Return'] = df['Price'].pct_change()
            
            # Keep only necessary columns
            df = df[['Date', 'Price', 'Return']].copy()
            
            print(f"✓ {asset_code:15s}: Loaded {len(df)} trading days")
            return df
            
        except Exception as e:
            print(f"✗ {asset_code:15s}: Error loading - {str(e)}")
            return None
    
    def load_all_assets(self) -> Dict[str, pd.DataFrame]:
        """
        Load all assets defined in ASSET_FILE_MAPPING.
        
        Returns:
            Dictionary mapping asset codes to DataFrames
        """
        print("\n" + "="*80)
        print("LOADING ASSET DATA")
        print("="*80)
        
        self.assets_data = {}
        
        for asset_code, filename in ASSET_FILE_MAPPING.items():
            df = self.load_single_asset(asset_code, filename)
            if df is not None:
                self.assets_data[asset_code] = df
        
        print(f"\n✓ Successfully loaded {len(self.assets_data)}/{len(ASSET_FILE_MAPPING)} assets")
        return self.assets_data
    
    def align_data(self) -> Tuple[pd.DataFrame, List[pd.Timestamp]]:
        """
        Align all assets to common trading dates.
        
        Returns:
            Tuple of (aligned_prices_df, common_dates_list)
        """
        if not self.assets_data:
            raise ValueError("No assets loaded. Call load_all_assets() first.")
        
        print("\n" + "="*80)
        print("ALIGNING DATA TO COMMON TRADING DATES")
        print("="*80)
        
        # Find common dates across all assets
        date_sets = [set(df['Date'].values) for df in self.assets_data.values()]
        self.common_dates = sorted(set.intersection(*date_sets))
        
        print(f"✓ Found {len(self.common_dates)} common trading days")
        print(f"  Date range: {self.common_dates[0].date()} to {self.common_dates[-1].date()}")
        
        # Create aligned price DataFrame
        aligned_prices = pd.DataFrame({'Date': self.common_dates})
        
        for asset_code, df in self.assets_data.items():
            # Filter to common dates and merge
            df_filtered = df[df['Date'].isin(self.common_dates)].copy()
            df_filtered = df_filtered.sort_values('Date')
            aligned_prices = aligned_prices.merge(
                df_filtered[['Date', 'Price']].rename(columns={'Price': asset_code}),
                on='Date',
                how='left'
            )
        
        aligned_prices = aligned_prices.set_index('Date')
        self.aligned_data = aligned_prices
        
        # Verify no missing values
        if self.aligned_data.isnull().any().any():
            print("  ⚠ Warning: Some missing values detected after alignment")
        
        return self.aligned_data, self.common_dates
    
    def get_returns_matrix(self) -> pd.DataFrame:
        """
        Calculate returns matrix from aligned price data.
        
        Returns:
            DataFrame of daily returns for all assets
        """
        if self.aligned_data is None:
            raise ValueError("Data not aligned. Call align_data() first.")
        
        returns = self.aligned_data.pct_change().dropna()
        return returns
    
    def get_correlation_matrix(self) -> pd.DataFrame:
        """
        Calculate correlation matrix of asset returns.
        
        Returns:
            Correlation matrix DataFrame
        """
        returns = self.get_returns_matrix()
        return returns.corr()
    
    def get_asset_statistics(self) -> pd.DataFrame:
        """
        Calculate basic statistics for all assets.
        
        Returns:
            DataFrame with mean return, volatility, and other stats
        """
        returns = self.get_returns_matrix()
        
        stats = pd.DataFrame({
            'Mean Daily Return': returns.mean(),
            'Daily Volatility': returns.std(),
            'Annualized Return': returns.mean() * 252,
            'Annualized Volatility': returns.std() * np.sqrt(252),
            'Min Return': returns.min(),
            'Max Return': returns.max(),
            'Skewness': returns.skew(),
            'Kurtosis': returns.kurtosis(),
        })
        
        return stats
    
    def summary(self) -> None:
        """
        Print summary of loaded data.
        """
        if not self.assets_data:
            print("No data loaded.")
            return
        
        print("\n" + "="*80)
        print("DATA SUMMARY")
        print("="*80)
        print(f"Total assets loaded: {len(self.assets_data)}")
        print(f"Common trading days: {len(self.common_dates) if self.common_dates else 'Not aligned'}")
        print(f"\nAssets:")
        for code in sorted(self.assets_data.keys()):
            name = ASSET_NAMES.get(code, code)
            print(f"  • {code:10s}: {name}")
