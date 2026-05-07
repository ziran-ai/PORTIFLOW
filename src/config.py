"""
Configuration module for portfolio analysis system.
Contains all configurable parameters, asset definitions, and portfolio specifications.
"""

import os
from pathlib import Path

# ============================================================================
# PROJECT PATHS
# ============================================================================

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "results"
VISUALIZATION_DIR = PROJECT_ROOT / "visualization"

# Create directories if they don't exist
RESULTS_DIR.mkdir(exist_ok=True)
VISUALIZATION_DIR.mkdir(exist_ok=True)

# ============================================================================
# BACKTEST PARAMETERS
# ============================================================================

INITIAL_CAPITAL = 1_000_000  # Initial capital in CNY
START_DATE = '2025-01-01'
END_DATE = '2025-12-31'
RISK_FREE_RATE = 0.02  # Annual risk-free rate (2%)

# ============================================================================
# ASSET DEFINITIONS
# ============================================================================

ASSET_FILE_MAPPING = {
    'CSI300': 'Shanghai Shenzhen CSI 300 Historical Data (2).csv',
    'HSI': 'Hang Seng Historical Data.csv',
    'SPX': 'S&P 500 Historical Data (1).csv',
    'NDX': 'Nasdaq 100 Historical Data.csv',
    'N225': 'Nikkei 225 Historical Data.csv',
    'SX5E': 'Euro Stoxx 50 Historical Data.csv',
    'GLD': 'GLD ETF Stock Price History.csv',
    'WTI': 'Crude Oil WTI Futures Historical Data.csv',
    'TLT': 'TLT ETF Stock Price History.csv',
    'CN10Y': 'China 10-Year Bond Yield Historical Data.csv',
    'VNQ': 'REIT ETF Stock Price History (1).csv',
    'BTC': 'BTC_USD Bitfinex Historical Data.csv',
    'Lead': 'Lead Futures Historical Data (1).csv',
    'Nickel': 'Nickel Futures Historical Data.csv',
}

ASSET_NAMES = {
    'CSI300': 'China A-Share CSI300',
    'HSI': 'Hong Kong Hang Seng Index',
    'SPX': 'US S&P 500',
    'NDX': 'US Nasdaq 100',
    'N225': 'Japan Nikkei 225',
    'SX5E': 'Europe STOXX 50',
    'GLD': 'Gold ETF',
    'WTI': 'WTI Crude Oil',
    'TLT': 'US Treasury Bond ETF',
    'CN10Y': 'China 10Y Government Bond',
    'VNQ': 'US REITs ETF',
    'BTC': 'Bitcoin',
    'Lead': 'Lead Futures',
    'Nickel': 'Nickel Futures',
}

# ============================================================================
# PORTFOLIO DEFINITIONS
# ============================================================================

PORTFOLIOS = {
    'Rate Cut Cycle Portfolio': {
        'GLD': 0.25,      # Gold benefits from rate cuts
        'NDX': 0.20,      # Growth stocks benefit from lower rates
        'TLT': 0.20,      # Bonds benefit from rate cuts
        'CN10Y': 0.20,    # China bonds
        'VNQ': 0.15,      # REITs benefit from lower rates
    },
    
    'AI Theme Portfolio': {
        'NDX': 0.30,      # AI-focused tech stocks
        'SPX': 0.20,      # Broad US market
        'HSI': 0.20,      # China tech exposure
        'N225': 0.15,     # Japan tech
        'SX5E': 0.15,     # Europe tech
    },
    
    'China Assets Portfolio': {
        'CSI300': 0.30,   # China A-shares
        'HSI': 0.25,      # Hong Kong stocks
        'GLD': 0.20,      # Gold hedge
        'CN10Y': 0.15,    # China bonds
        'Lead': 0.10,     # Industrial metals
    },
    
    'Global Equity Portfolio': {
        'SPX': 0.25,      # US market
        'SX5E': 0.20,     # Europe market
        'N225': 0.20,     # Japan market
        'HSI': 0.20,      # Hong Kong market
        'CSI300': 0.15,   # China market
    },
    
    'Balanced Portfolio': {
        'GLD': 0.20,      # Gold
        'NDX': 0.15,      # Growth stocks
        'HSI': 0.15,      # Hong Kong stocks
        'TLT': 0.20,      # US bonds
        'CN10Y': 0.15,    # China bonds
        'VNQ': 0.15,      # REITs
    },
    
    'Equal Weight Benchmark': {
        asset: 1.0/14 for asset in ASSET_FILE_MAPPING.keys()
    },
    
    '60/40 Portfolio': {
        'SPX': 0.25,      # 25% US stocks
        'NDX': 0.25,      # 25% US tech
        'TLT': 0.30,      # 30% US bonds
        'CN10Y': 0.10,    # 10% China bonds
        'GLD': 0.10,      # 10% Gold
    },
}

# ============================================================================
# VISUALIZATION SETTINGS
# ============================================================================

COLOR_PALETTE = {
    'lavender': '#9B8FD9',
    'coral': '#E07A7A',
    'mint': '#7AD0B0',
    'sky_blue': '#6BADEA',
    'warm_orange': '#F4A261',
    'cream_yellow': '#FCE49C',
    'grey_blue': '#8FB9C7',
    'bean_pink': '#D4A5A5',
}

CHART_COLORS = list(COLOR_PALETTE.values())

MATPLOTLIB_STYLE = {
    'figure.figsize': (16, 10),
    'figure.dpi': 100,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 11,
    'figure.titlesize': 18,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'axes.facecolor': '#FAFAFA',
    'figure.facecolor': 'white',
}

# ============================================================================
# PERFORMANCE METRICS
# ============================================================================

METRICS_TO_CALCULATE = [
    'initial_capital',
    'final_value',
    'total_return',
    'total_return_pct',
    'annualized_return',
    'annualized_volatility',
    'sharpe_ratio',
    'sortino_ratio',
    'max_drawdown',
    'calmar_ratio',
    'win_rate',
    'var_95',
]

# ============================================================================
# CHART SPECIFICATIONS
# ============================================================================

CHARTS_TO_GENERATE = [
    'correlation_heatmap',
    'portfolio_values',
    'drawdown_curves',
    'cumulative_returns',
    'efficient_frontier',
    'performance_metrics',
    'portfolio_allocations',
    'returns_distribution',
    'rolling_sharpe',
    'monthly_returns_heatmap',
]
