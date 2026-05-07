# Setup Guide

This guide will help you set up the Global Asset Portfolio Analysis System on your machine.

## Prerequisites

- **Python**: Version 3.8 or higher
- **pip**: Python package installer
- **Git**: For cloning the repository (optional)

## Installation Steps

### 1. Clone or Download the Repository

**Option A: Using Git**
```bash
git clone https://github.com/yourusername/global-portfolio-analysis.git
cd global-portfolio-analysis
```

**Option B: Download ZIP**
- Download the ZIP file from GitHub
- Extract to your desired location
- Navigate to the extracted folder

### 2. Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- pandas (data manipulation)
- numpy (numerical computing)
- matplotlib (plotting)
- seaborn (statistical visualization)
- scipy (scientific computing)
- And other required packages

### 4. Prepare Your Data

Place your CSV data files in the `data/` directory. Files should be named according to the mapping in `src/config.py`:

```
data/
├── Shanghai Shenzhen CSI 300 Historical Data (2).csv
├── Hang Seng Historical Data.csv
├── S&P 500 Historical Data (1).csv
├── Nasdaq 100 Historical Data.csv
├── Nikkei 225 Historical Data.csv
├── Euro Stoxx 50 Historical Data.csv
├── GLD ETF Stock Price History.csv
├── Crude Oil WTI Futures Historical Data.csv
├── TLT ETF Stock Price History.csv
├── China 10-Year Bond Yield Historical Data.csv
├── REIT ETF Stock Price History (1).csv
├── BTC_USD Bitfinex Historical Data.csv
├── Lead Futures Historical Data (1).csv
└── Nickel Futures Historical Data.csv
```

**CSV Format Requirements:**
- Must have `Date` column in MM/DD/YYYY format
- Must have `Price` column with closing prices
- Other columns (Open, High, Low, Volume) are optional

### 5. Verify Installation

Run a quick test to ensure everything is set up correctly:

```bash
python -c "from src.data_loader import DataLoader; print('Setup successful!')"
```

If you see "Setup successful!", you're ready to go!

## Running the Analysis

### Basic Usage

Run the complete analysis pipeline:

```bash
python main.py
```

This will:
1. Load all asset data
2. Backtest all 7 portfolios
3. Generate 10+ visualizations
4. Save results to `results/` and `visualization/` directories

### Running Examples

Explore the example scripts in the `examples/` directory:

```bash
# Analyze asset data and correlations
python examples/data_analysis_example.py

# Create and backtest a custom portfolio
python examples/custom_portfolio_example.py
```

## Configuration

### Customizing Portfolios

Edit `src/config.py` to modify portfolio allocations:

```python
PORTFOLIOS = {
    'My Custom Portfolio': {
        'SPX': 0.60,   # 60% S&P 500
        'GLD': 0.30,   # 30% Gold
        'TLT': 0.10,   # 10% Bonds
    },
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

Modify visualization settings in `src/config.py`:

```python
COLOR_PALETTE = {
    'lavender': '#9B8FD9',
    'coral': '#E07A7A',
    # Add your custom colors...
}

MATPLOTLIB_STYLE = {
    'figure.figsize': (16, 10),
    'savefig.dpi': 300,
    # Customize plot style...
}
```

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'src'`
- **Solution**: Make sure you're running scripts from the project root directory

**Issue**: `FileNotFoundError` when loading data
- **Solution**: 
  - Verify CSV files are in the `data/` directory
  - Check filenames match those in `src/config.py`
  - Ensure file paths use correct separators for your OS

**Issue**: `ValueError: Portfolio weights must sum to 1.0`
- **Solution**: Check that portfolio weights in `src/config.py` sum to exactly 1.0

**Issue**: Insufficient data error
- **Solution**: 
  - Ensure CSV files contain at least 100 trading days
  - Verify date range overlaps with START_DATE and END_DATE
  - Check date format is MM/DD/YYYY

**Issue**: Import errors with matplotlib on macOS
- **Solution**: 
  ```bash
  pip install --upgrade matplotlib
  # If still fails, try:
  pip uninstall matplotlib
  pip install matplotlib
  ```

### Getting Help

If you encounter issues:
1. Check the [README](README_EN.md) for detailed documentation
2. Review the [examples](examples/) for usage patterns
3. Open an issue on GitHub with:
   - Error message
   - Steps to reproduce
   - Your environment (Python version, OS)

## Next Steps

Once setup is complete:

1. **Explore the code**: Start with `main.py` to understand the pipeline
2. **Run examples**: Try the example scripts in `examples/`
3. **Customize**: Modify portfolios and parameters in `src/config.py`
4. **Analyze**: Review results in `results/` and `visualization/`
5. **Extend**: Add new assets, metrics, or visualizations

## Updating

To update to the latest version:

```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

## Uninstalling

To remove the virtual environment and clean up:

```bash
# Deactivate virtual environment
deactivate

# Remove virtual environment directory
rm -rf venv  # On macOS/Linux
rmdir /s venv  # On Windows

# Optionally remove generated files
rm -rf results/* visualization/*
```

---

**Happy analyzing! 📊**
