# Global Asset Portfolio Analysis System

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive, production-ready framework for global asset portfolio backtesting, optimization, and visualization.

## 🌟 Features

- **Multi-Asset Support**: Analyze 14+ global assets including equities, bonds, commodities, and cryptocurrencies
- **Modular Architecture**: Clean, maintainable code with separation of concerns
- **7 Pre-configured Portfolios**: From conservative to aggressive strategies
- **Comprehensive Metrics**: 11+ performance indicators including Sharpe, Sortino, Calmar ratios
- **Professional Visualizations**: 10+ publication-quality charts and plots
- **Flexible Configuration**: Easy-to-modify portfolio weights and parameters
- **Production Ready**: Type hints, docstrings, error handling, and logging

## 📊 Supported Assets

| Category | Assets |
|----------|--------|
| **China Equities** | CSI300, Hang Seng Index |
| **US Equities** | S&P 500, Nasdaq 100 |
| **International Equities** | Nikkei 225, Euro STOXX 50 |
| **Fixed Income** | US Treasury ETF (TLT), China 10Y Government Bond |
| **Commodities** | Gold (GLD), WTI Crude Oil, Lead Futures, Nickel Futures |
| **Real Estate** | US REITs ETF (VNQ) |
| **Cryptocurrency** | Bitcoin (BTC) |

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/global-portfolio-analysis.git
cd global-portfolio-analysis
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Prepare your data**
   - Place CSV files in the `data/` directory
   - Ensure files match the naming convention in `src/config.py`

4. **Run the analysis**
```bash
python main.py
```

### Expected Output

The system will generate:
- **Results**: CSV files in `results/` directory
  - `backtest_summary.csv`: Overall portfolio performance
  - `*_details.csv`: Detailed daily data for each portfolio
  
- **Visualizations**: PNG files in `visualization/` directory
  - Correlation heatmap
  - Portfolio value curves
  - Drawdown analysis
  - Efficient frontier
  - Performance metrics comparison
  - And more...

## 📁 Project Structure

```
global-portfolio-analysis/
├── main.py                 # Main entry point
├── src/                    # Source code modules
│   ├── __init__.py
│   ├── config.py          # Configuration and constants
│   ├── data_loader.py     # Data loading and preprocessing
│   ├── backtest_engine.py # Portfolio backtesting engine
│   └── visualizer.py      # Visualization generation
├── data/                   # Asset price data (CSV files)
├── results/                # Backtest results (generated)
├── visualization/          # Charts and plots (generated)
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🎯 Pre-configured Portfolios

### 1. Rate Cut Cycle Portfolio
**Strategy**: Benefits from global monetary easing  
**Allocation**: Gold (25%), Nasdaq 100 (20%), US Bonds (20%), China Bonds (20%), REITs (15%)  
**Risk Level**: Medium  
**Expected Return**: 12-18% annually

### 2. AI Theme Portfolio
**Strategy**: Focused on artificial intelligence and technology  
**Allocation**: Nasdaq 100 (30%), S&P 500 (20%), Hang Seng (20%), Nikkei 225 (15%), Euro STOXX 50 (15%)  
**Risk Level**: High  
**Expected Return**: 20-30% annually

### 3. China Assets Portfolio
**Strategy**: Exposure to China's economic recovery  
**Allocation**: CSI300 (30%), Hang Seng (25%), Gold (20%), China Bonds (15%), Lead Futures (10%)  
**Risk Level**: Medium-High  
**Expected Return**: 15-25% annually

### 4. Global Equity Portfolio
**Strategy**: Diversified global stock exposure  
**Allocation**: S&P 500 (25%), Euro STOXX 50 (20%), Nikkei 225 (20%), Hang Seng (20%), CSI300 (15%)  
**Risk Level**: Medium  
**Expected Return**: 15-22% annually

### 5. Balanced Portfolio
**Strategy**: Balanced risk-return profile  
**Allocation**: Gold (20%), Nasdaq 100 (15%), Hang Seng (15%), US Bonds (20%), China Bonds (15%), REITs (15%)  
**Risk Level**: Medium-Low  
**Expected Return**: 10-15% annually

### 6. Equal Weight Benchmark
**Strategy**: Passive diversification baseline  
**Allocation**: All 14 assets equally weighted  
**Risk Level**: Medium-Low  
**Expected Return**: 8-12% annually

### 7. 60/40 Portfolio
**Strategy**: Classic stock-bond allocation  
**Allocation**: 60% Stocks (S&P 500, Nasdaq 100), 40% Bonds (US, China) + Gold  
**Risk Level**: Medium  
**Expected Return**: 10-14% annually

## 📈 Performance Metrics

The system calculates the following metrics for each portfolio:

| Metric | Description |
|--------|-------------|
| **Total Return** | Absolute profit/loss in CNY |
| **Total Return %** | Percentage gain/loss |
| **Annualized Return** | Compound annual growth rate |
| **Annualized Volatility** | Standard deviation of returns (annualized) |
| **Sharpe Ratio** | Risk-adjusted return (excess return / volatility) |
| **Sortino Ratio** | Downside risk-adjusted return |
| **Maximum Drawdown** | Largest peak-to-trough decline |
| **Calmar Ratio** | Return / absolute max drawdown |
| **Win Rate** | Percentage of positive return days |
| **VaR 95%** | Value at Risk at 95% confidence level |

## 🎨 Visualizations

The system generates 10+ professional charts:

1. **Correlation Heatmap**: Asset correlation matrix
2. **Portfolio Values**: Net asset value over time
3. **Drawdown Curves**: Underwater equity curves
4. **Cumulative Returns**: Return accumulation over time
5. **Efficient Frontier**: Risk-return scatter plot
6. **Performance Metrics**: Bar chart comparisons
7. **Portfolio Allocations**: Pie charts for each portfolio
8. **Returns Distribution**: Histogram of daily returns
9. **Rolling Sharpe Ratio**: Time-varying risk-adjusted performance
10. **Monthly Returns Heatmap**: Calendar view of returns

## ⚙️ Configuration

### Customizing Portfolios

Edit `src/config.py` to modify portfolio allocations:

```python
PORTFOLIOS = {
    'My Custom Portfolio': {
        'SPX': 0.40,    # 40% S&P 500
        'GLD': 0.30,    # 30% Gold
        'TLT': 0.30,    # 30% US Bonds
    },
    # Add more portfolios...
}
```

### Adjusting Parameters

Key parameters in `src/config.py`:

```python
INITIAL_CAPITAL = 1_000_000  # Starting capital (CNY)
START_DATE = '2025-01-01'    # Backtest start date
END_DATE = '2025-12-31'      # Backtest end date
RISK_FREE_RATE = 0.02        # Annual risk-free rate (2%)
```

### Customizing Visualizations

Modify visualization settings:

```python
COLOR_PALETTE = {
    'lavender': '#9B8FD9',
    'coral': '#E07A7A',
    # Add your colors...
}

MATPLOTLIB_STYLE = {
    'figure.figsize': (16, 10),
    'savefig.dpi': 300,
    # Customize plot style...
}
```

## 🔧 Advanced Usage

### Using Individual Modules

```python
from src.data_loader import DataLoader
from src.backtest_engine import BacktestEngine
from src.visualizer import PortfolioVisualizer

# Load data
loader = DataLoader()
assets = loader.load_all_assets()
aligned_data, dates = loader.align_data()

# Backtest a custom portfolio
engine = BacktestEngine(initial_capital=1_000_000)
weights = {'SPX': 0.6, 'TLT': 0.4}
values, returns = engine.backtest_portfolio('My Portfolio', weights, aligned_data)
metrics = engine.calculate_metrics('My Portfolio')

# Generate visualizations
viz = PortfolioVisualizer()
viz.plot_portfolio_values({'My Portfolio': values})
```

### Extending the System

To add new assets:

1. Add CSV file to `data/` directory
2. Update `ASSET_FILE_MAPPING` in `src/config.py`
3. Update `ASSET_NAMES` for display names

To add new metrics:

1. Extend `PortfolioMetrics` dataclass in `src/backtest_engine.py`
2. Add calculation logic in `calculate_metrics()` method
3. Update visualization code if needed

## 📊 Data Format

CSV files should have the following format:

```csv
Date,Price,Open,High,Low,Vol.,Change %
12/31/2025,4500.50,4480.00,4520.00,4475.00,2.5B,0.45%
12/30/2025,4480.00,4470.00,4490.00,4465.00,2.3B,0.22%
...
```

Required columns:
- `Date`: MM/DD/YYYY format
- `Price`: Closing price (numeric, may contain commas)

## 🐛 Troubleshooting

### Common Issues

**Issue**: `FileNotFoundError` when loading data
- **Solution**: Ensure CSV files are in `data/` directory with correct filenames

**Issue**: `ValueError: Portfolio weights must sum to 1.0`
- **Solution**: Check portfolio weights in `src/config.py` sum to exactly 1.0

**Issue**: Insufficient data error
- **Solution**: Ensure CSV files contain at least 100 trading days in the specified date range

**Issue**: Missing values after alignment
- **Solution**: Check that all assets have data for common trading dates

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

## 🙏 Acknowledgments

- Modern Portfolio Theory by Harry Markowitz
- Sharpe Ratio by William F. Sharpe
- Data sources: Yahoo Finance, Investing.com, and other public sources

## 📚 Citation

If you use this project in your research, please cite:

```bibtex
@software{global_portfolio_analysis,
  title = {Global Asset Portfolio Analysis System},
  author = {Portfolio Research Team},
  year = {2025},
  url = {https://github.com/yourusername/global-portfolio-analysis}
}
```

---

**Built with ❤️ for portfolio optimization and financial analysis**
