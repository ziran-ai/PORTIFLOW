# Project Structure

This document provides a comprehensive overview of the Global Asset Portfolio Analysis System's organization.

## Directory Tree

```
global-portfolio-analysis/
│
├── main.py                          # Main entry point - run this to execute full analysis
│
├── src/                             # Source code modules
│   ├── __init__.py                  # Package initialization
│   ├── config.py                    # Configuration and constants
│   ├── data_loader.py               # Data loading and preprocessing
│   ├── backtest_engine.py           # Portfolio backtesting engine
│   └── visualizer.py                # Visualization generation
│
├── data/                            # Asset price data (CSV files)
│   ├── Shanghai Shenzhen CSI 300 Historical Data (2).csv
│   ├── Hang Seng Historical Data.csv
│   ├── S&P 500 Historical Data (1).csv
│   ├── Nasdaq 100 Historical Data.csv
│   ├── Nikkei 225 Historical Data.csv
│   ├── Euro Stoxx 50 Historical Data.csv
│   ├── GLD ETF Stock Price History.csv
│   ├── Crude Oil WTI Futures Historical Data.csv
│   ├── TLT ETF Stock Price History.csv
│   ├── China 10-Year Bond Yield Historical Data.csv
│   ├── REIT ETF Stock Price History (1).csv
│   ├── BTC_USD Bitfinex Historical Data.csv
│   ├── Lead Futures Historical Data (1).csv
│   └── Nickel Futures Historical Data.csv
│
├── results/                         # Generated backtest results (CSV)
│   ├── .gitkeep                     # Ensures directory is tracked
│   ├── backtest_summary.csv         # Overall portfolio performance summary
│   └── *_details.csv                # Detailed daily data for each portfolio
│
├── visualization/                   # Generated charts and plots (PNG)
│   ├── .gitkeep                     # Ensures directory is tracked
│   ├── 01_correlation_heatmap.png
│   ├── 02_portfolio_values.png
│   ├── 03_drawdown_curves.png
│   ├── 04_cumulative_returns.png
│   ├── 05_efficient_frontier.png
│   ├── 07_performance_metrics.png
│   ├── 08_portfolio_allocations.png
│   ├── 09_returns_distribution.png
│   ├── 10_rolling_sharpe.png
│   └── 11_monthly_returns_heatmap.png
│
├── examples/                        # Example scripts and tutorials
│   ├── README.md                    # Examples documentation
│   ├── data_analysis_example.py     # Asset data analysis example
│   └── custom_portfolio_example.py  # Custom portfolio creation example
│
├── docs/                            # Additional documentation (optional)
│   └── (research papers, methodology notes, etc.)
│
├── README.md                        # Chinese project overview
├── README_EN.md                     # English project documentation (main)
├── SETUP.md                         # Installation and setup guide
├── CONTRIBUTING.md                  # Contribution guidelines
├── CHANGELOG.md                     # Version history and changes
├── LICENSE                          # MIT License
├── .gitignore                       # Git ignore rules
└── requirements.txt                 # Python dependencies
```

## Module Descriptions

### Core Modules (`src/`)

#### `config.py`
**Purpose**: Central configuration file for the entire system.

**Contents**:
- Project paths (data, results, visualization directories)
- Backtest parameters (initial capital, date range, risk-free rate)
- Asset definitions (file mappings, display names)
- Portfolio specifications (7 pre-configured portfolios)
- Visualization settings (colors, chart styles)
- Performance metrics list
- Chart specifications

**Key Constants**:
- `INITIAL_CAPITAL`: Starting capital (1,000,000 CNY)
- `START_DATE`, `END_DATE`: Backtest period (2025)
- `PORTFOLIOS`: Dictionary of all portfolio allocations
- `COLOR_PALETTE`: Custom color scheme for charts

---

#### `data_loader.py`
**Purpose**: Handles all data loading, cleaning, and preprocessing.

**Main Class**: `DataLoader`

**Key Methods**:
- `load_all_assets()`: Load all CSV files from data directory
- `load_single_asset()`: Load and clean a single asset's data
- `align_data()`: Align all assets to common trading dates
- `get_returns_matrix()`: Calculate daily returns for all assets
- `get_correlation_matrix()`: Compute asset correlation matrix
- `get_asset_statistics()`: Generate summary statistics

**Features**:
- Automatic data cleaning (removes commas, handles missing values)
- Date parsing and validation
- Duplicate date removal
- Data alignment across assets
- Error handling and logging

---

#### `backtest_engine.py`
**Purpose**: Portfolio backtesting and performance calculation.

**Main Class**: `BacktestEngine`

**Data Class**: `PortfolioMetrics` (stores all performance metrics)

**Key Methods**:
- `backtest_portfolio()`: Backtest a single portfolio
- `backtest_all_portfolios()`: Backtest multiple portfolios
- `calculate_metrics()`: Compute 11+ performance metrics
- `get_summary_dataframe()`: Generate results summary table
- `get_drawdown_series()`: Calculate drawdown over time
- `get_rolling_sharpe()`: Compute rolling Sharpe ratio

**Calculated Metrics**:
1. Total Return (absolute and percentage)
2. Annualized Return
3. Annualized Volatility
4. Sharpe Ratio
5. Sortino Ratio
6. Maximum Drawdown
7. Calmar Ratio
8. Win Rate
9. Value at Risk (95%)
10. Number of Assets

---

#### `visualizer.py`
**Purpose**: Generate professional visualizations for analysis results.

**Main Class**: `PortfolioVisualizer`

**Key Methods**:
- `plot_correlation_heatmap()`: Asset correlation matrix
- `plot_portfolio_values()`: Net asset value curves
- `plot_drawdown_curves()`: Underwater equity curves
- `plot_cumulative_returns()`: Return accumulation
- `plot_efficient_frontier()`: Risk-return scatter plot
- `plot_performance_metrics()`: Bar chart comparisons
- `plot_portfolio_allocations()`: Pie charts for allocations
- `plot_returns_distribution()`: Return histograms
- `plot_rolling_sharpe()`: Time-varying Sharpe ratio
- `plot_monthly_returns_heatmap()`: Calendar view of returns

**Features**:
- Publication-quality charts (300 DPI)
- Consistent color scheme
- Professional styling
- Automatic saving to visualization directory

---

### Main Entry Point

#### `main.py`
**Purpose**: Orchestrates the complete analysis pipeline.

**Workflow**:
1. **Load Data**: Initialize DataLoader and load all assets
2. **Backtest**: Run backtesting for all portfolios
3. **Visualize**: Generate all charts and plots
4. **Save Results**: Export CSV summaries and detailed data

**Usage**:
```bash
python main.py
```

---

### Examples (`examples/`)

#### `data_analysis_example.py`
Demonstrates:
- Loading and exploring asset data
- Calculating correlations
- Generating statistics
- Identifying top/bottom performers

#### `custom_portfolio_example.py`
Demonstrates:
- Defining custom portfolios
- Running backtests
- Generating visualizations
- Interpreting results

---

## Data Flow

```
CSV Files (data/)
    ↓
DataLoader.load_all_assets()
    ↓
DataLoader.align_data()
    ↓
Aligned Price Data
    ↓
BacktestEngine.backtest_all_portfolios()
    ↓
Portfolio Values & Returns
    ↓
BacktestEngine.calculate_metrics()
    ↓
Performance Metrics
    ↓
PortfolioVisualizer.plot_*()
    ↓
Charts (visualization/) & Results (results/)
```

## Configuration Flow

```
src/config.py
    ↓
├─→ PORTFOLIOS → BacktestEngine
├─→ ASSET_FILE_MAPPING → DataLoader
├─→ COLOR_PALETTE → PortfolioVisualizer
├─→ INITIAL_CAPITAL → BacktestEngine
└─→ START_DATE, END_DATE → DataLoader
```

## Output Files

### Results Directory (`results/`)

**backtest_summary.csv**
- Overall performance summary for all portfolios
- Columns: Portfolio, Initial Capital, Final Value, Returns, Sharpe, etc.
- Sorted by Sharpe Ratio (descending)

**{Portfolio_Name}_details.csv**
- Daily data for each portfolio
- Columns: Date, Portfolio Value, Daily Return, Cumulative Return

### Visualization Directory (`visualization/`)

All charts are saved as high-resolution PNG files (300 DPI):

1. **01_correlation_heatmap.png**: 14×14 asset correlation matrix
2. **02_portfolio_values.png**: Portfolio NAV over time
3. **03_drawdown_curves.png**: Drawdown analysis
4. **04_cumulative_returns.png**: Cumulative return curves
5. **05_efficient_frontier.png**: Risk-return scatter plot
6. **07_performance_metrics.png**: 2×2 bar chart comparison
7. **08_portfolio_allocations.png**: Pie charts for all portfolios
8. **09_returns_distribution.png**: Return histograms
9. **10_rolling_sharpe.png**: Rolling Sharpe ratio curves
10. **11_monthly_returns_heatmap.png**: Monthly returns calendar

## Extending the System

### Adding a New Asset

1. Add CSV file to `data/` directory
2. Update `ASSET_FILE_MAPPING` in `src/config.py`
3. Update `ASSET_NAMES` dictionary
4. Run `python main.py`

### Adding a New Portfolio

1. Edit `PORTFOLIOS` in `src/config.py`
2. Add portfolio definition with weights summing to 1.0
3. Run `python main.py`

### Adding a New Metric

1. Add field to `PortfolioMetrics` dataclass in `src/backtest_engine.py`
2. Implement calculation in `calculate_metrics()` method
3. Update `get_summary_dataframe()` to include new metric
4. Update visualizations if needed

### Adding a New Visualization

1. Add method to `PortfolioVisualizer` class in `src/visualizer.py`
2. Follow naming convention: `plot_<chart_name>()`
3. Save to `VISUALIZATION_DIR` with numbered filename
4. Call from `main.py` in Step 3

## Dependencies

See `requirements.txt` for full list. Key dependencies:

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Plotting and visualization
- **seaborn**: Statistical data visualization
- **scipy**: Scientific computing
- **statsmodels**: Statistical modeling

## Best Practices

### Code Style
- Follow PEP 8 guidelines
- Use type hints for function parameters
- Write comprehensive docstrings
- Use English for all comments and documentation

### Data Management
- Keep raw data in `data/` directory
- Never modify original CSV files
- Use `.gitignore` to exclude generated files

### Version Control
- Commit code changes regularly
- Use meaningful commit messages
- Keep data files separate from code

### Testing
- Test with small datasets first
- Verify results manually for sanity checks
- Check edge cases (missing data, zero weights, etc.)

## Common Workflows

### Standard Analysis
```bash
python main.py
```

### Custom Portfolio Analysis
```bash
python examples/custom_portfolio_example.py
```

### Data Exploration
```bash
python examples/data_analysis_example.py
```

### Batch Processing
```python
# Create multiple custom portfolios
portfolios = {
    'Portfolio 1': {...},
    'Portfolio 2': {...},
    'Portfolio 3': {...},
}
engine.backtest_all_portfolios(portfolios, aligned_data)
```

---

**For more information, see:**
- [README_EN.md](README_EN.md) - Main documentation
- [SETUP.md](SETUP.md) - Installation guide
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [examples/README.md](examples/README.md) - Example scripts
