# Contributing to Global Asset Portfolio Analysis System

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (Python version, OS, etc.)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please open an issue with:
- Clear description of the enhancement
- Use case and benefits
- Possible implementation approach (optional)

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the code style guidelines below
   - Add tests if applicable
   - Update documentation as needed

4. **Test your changes**
   ```bash
   python main.py  # Ensure the main pipeline works
   ```

5. **Commit your changes**
   ```bash
   git commit -m "Add feature: brief description"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Provide a clear description of changes
   - Reference any related issues

## Code Style Guidelines

### Python Code Style

- Follow PEP 8 style guide
- Use type hints for function parameters and return values
- Write docstrings for all public functions and classes
- Keep functions focused and under 50 lines when possible
- Use meaningful variable names

**Example:**

```python
def calculate_sharpe_ratio(
    returns: pd.Series,
    risk_free_rate: float = 0.02
) -> float:
    """
    Calculate Sharpe ratio for a return series.
    
    Args:
        returns: Series of daily returns
        risk_free_rate: Annual risk-free rate (default: 2%)
        
    Returns:
        Sharpe ratio value
    """
    excess_return = returns.mean() * 252 - risk_free_rate
    volatility = returns.std() * np.sqrt(252)
    return excess_return / volatility if volatility > 0 else 0
```

### Documentation

- Use English for all code comments and documentation
- Write clear, concise docstrings
- Update README.md if adding new features
- Include examples in docstrings when helpful

### Commit Messages

Use clear, descriptive commit messages:

- `feat: Add new portfolio optimization algorithm`
- `fix: Correct Sharpe ratio calculation`
- `docs: Update README with new examples`
- `refactor: Simplify data loading logic`
- `test: Add unit tests for backtest engine`

## Project Structure

When adding new features, maintain the modular structure:

```
src/
├── config.py          # Configuration and constants
├── data_loader.py     # Data loading and preprocessing
├── backtest_engine.py # Backtesting logic
└── visualizer.py      # Visualization generation
```

## Testing

While we don't have formal unit tests yet, please ensure:
- Your code runs without errors
- Results are reasonable and expected
- Edge cases are handled (empty data, missing values, etc.)

## Adding New Assets

To add support for a new asset:

1. Add CSV file to `data/` directory
2. Update `ASSET_FILE_MAPPING` in `src/config.py`
3. Update `ASSET_NAMES` dictionary
4. Test with a sample portfolio

## Adding New Metrics

To add a new performance metric:

1. Add field to `PortfolioMetrics` dataclass in `src/backtest_engine.py`
2. Implement calculation in `calculate_metrics()` method
3. Update `get_summary_dataframe()` to include new metric
4. Update visualization code if needed

## Adding New Visualizations

To add a new chart:

1. Add method to `PortfolioVisualizer` class in `src/visualizer.py`
2. Follow naming convention: `plot_<chart_name>()`
3. Save to `VISUALIZATION_DIR` with descriptive filename
4. Call from `main.py` in appropriate section

## Questions?

Feel free to open an issue for any questions about contributing!

## Code of Conduct

- Be respectful and constructive
- Welcome newcomers and help them learn
- Focus on what is best for the project
- Show empathy towards other contributors

Thank you for contributing! 🎉
