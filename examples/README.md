# Examples

This directory contains example scripts demonstrating how to use the Global Asset Portfolio Analysis System.

## Available Examples

### 1. Data Analysis Example
**File**: `data_analysis_example.py`

Demonstrates how to:
- Load and explore asset data
- Calculate correlation matrices
- Generate asset statistics
- Identify top and bottom performers

**Run**:
```bash
python examples/data_analysis_example.py
```

### 2. Custom Portfolio Example
**File**: `custom_portfolio_example.py`

Demonstrates how to:
- Define a custom portfolio
- Run backtesting
- Calculate performance metrics
- Generate visualizations

**Run**:
```bash
python examples/custom_portfolio_example.py
```

## Creating Your Own Examples

To create a new example:

1. Create a new Python file in this directory
2. Add the path setup code:
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
```

3. Import the modules you need:
```python
from src.data_loader import DataLoader
from src.backtest_engine import BacktestEngine
from src.visualizer import PortfolioVisualizer
```

4. Write your analysis code
5. Run from the project root directory

## Common Patterns

### Loading Data
```python
loader = DataLoader()
loader.load_all_assets()
aligned_data, dates = loader.align_data()
```

### Backtesting a Portfolio
```python
engine = BacktestEngine(initial_capital=1_000_000)
portfolio = {'My Portfolio': {'SPX': 0.6, 'GLD': 0.4}}
engine.backtest_all_portfolios(portfolio, aligned_data)
metrics = engine.portfolio_metrics['My Portfolio']
```

### Generating Visualizations
```python
viz = PortfolioVisualizer()
viz.plot_portfolio_values(engine.portfolio_values)
viz.plot_drawdown_curves({name: engine.get_drawdown_series(name) for name in portfolio.keys()})
```

## Tips

- Always run examples from the project root directory
- Check that your data files are in the `data/` directory
- Results will be saved to `results/` and `visualization/` directories
- Modify the examples to experiment with different portfolios and parameters

## Need Help?

- Check the main [README](../README_EN.md) for detailed documentation
- Review the [SETUP](../SETUP.md) guide for installation help
- Open an issue on GitHub if you encounter problems
