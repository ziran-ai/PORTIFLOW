# 现代投资组合分析系统

## 📊 项目概述

本项目实现了一个完整的现代投资组合分析系统，涵盖从宏观研究到回测验证的全流程分析。

**项目特点**：
- ✅ 全球视角的宏观经济研究（8000字）
- ✅ 系统化的因子驱动分析框架
- ✅ 5个投资组合设计（3条主线+2个对照组）
- ✅ 5种交易策略实现
- ✅ 完整的回测引擎（25个组合×策略组合）
- ✅ 压力测试（5个极端情景）
- ✅ Brinson归因分析
- ✅ 20+张专业可视化图表
- ✅ 自定义配色方案

---

## 🎯 项目进度

### ✅ 已完成（Phase 0-9）

| 阶段 | 内容 | 状态 |
|------|------|------|
| **Phase 0** | 数据获取 | ✓ 完成 |
| **Phase 1** | 宏观研究报告（8000字） | ✓ 完成 |
| **Phase 2** | 因子驱动矩阵（4000字） | ✓ 完成 |
| **Phase 3** | 投资组合构建（6000字） | ✓ 完成 |
| **Phase 4** | 相关性分析代码 | ✓ 完成 |
| **Phase 5** | 交易策略代码 | ✓ 完成 |
| **Phase 6** | 回测引擎代码 | ✓ 完成 |
| **Phase 7** | 压力测试代码 | ✓ 完成 |
| **Phase 8** | Brinson归因代码 | ✓ 完成 |
| **Phase 9** | 完整可视化代码 | ✓ 完成 |

### ⏳ 待完成（Phase 10）

| 阶段 | 内容 | 状态 |
|------|------|------|
| **Phase 10** | 论文撰写（10页） | 待完成 |

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 准备数据

将数据文件放入 `data/` 文件夹：
```
data/
├── CSI300_2025.csv
├── HSI_2025.csv
├── SPX_2025.csv
├── GOLD_2025.csv
└── ...
```

### 3. 运行完整分析

```bash
python run_complete_analysis.py
```

这将自动执行：
- ✅ 数据加载与对齐
- ✅ 相关性分析
- ✅ 回测所有组合×策略（5×5=25个）
- ✅ 压力测试（5个情景）
- ✅ Brinson归因分析
- ✅ 生成20+张可视化图表
- ✅ 保存所有结果

**预计运行时间**: 5-10分钟（取决于数据量）

---

## 📁 项目结构

```
结课论文/
│
├── 📄 核心代码模块
│   ├── data_loader.py                    # 数据加载
│   ├── correlation_analysis.py           # 相关性分析
│   ├── trading_strategies.py             # 交易策略
│   ├── backtesting_engine.py             # 回测引擎
│   ├── stress_testing.py                 # 压力测试
│   ├── brinson_attribution.py            # Brinson归因
│   ├── comprehensive_visualization.py    # 可视化
│   └── visualization_config.py           # 配色配置
│
├── 📄 执行脚本
│   ├── main_analysis.py                  # 主分析脚本（Phase 4-6）
│   └── run_complete_analysis.py          # 完整分析脚本（Phase 4-9）
│
├── 📄 配置文件
│   ├── portfolios_config.json            # 投资组合配置
│   └── requirements.txt                  # Python依赖
│
├── 📁 研究文档
│   └── docs/
│       ├── macro_research_2025.md        # 宏观研究（8000字）
│       ├── factor_matrix.md              # 因子矩阵（4000字）
│       └── portfolio_construction.md     # 组合构建（6000字）
│
├── 📁 数据文件夹
│   ├── data/                             # 原始数据
│   └── processed_data/                   # 处理后数据
│
├── 📁 输出结果
│   ├── results/                          # 分析结果
│   └── visualization/                    # 可视化图表
│
└── 📄 文档
    ├── README.md                         # 本文件
    ├── QUICKSTART.md                     # 快速开始指南
    ├── IMPLEMENTATION_GUIDE.md           # 实施指南
    └── PROJECT_PROGRESS.md               # 项目进度
```

---

## 💡 核心功能

### 1. 投资组合设计

#### **主线A: 降息周期多资产配置**（推荐）
- **配置**: 黄金25% + 美股科技20% + 港股20% + 中国债券20% + A股成长10% + REITs5%
- **逻辑**: 哑铃型配置，黄金+债券提供安全垫，成长股提供进攻性
- **预期**: 收益12-18%，夏普1.0-1.2，风险中等

#### **主线B: AI主题驱动**（进攻型）
- **配置**: 美股科技40% + 港股科技25% + A股半导体20% + A股消费电子10% + 比特币5%
- **逻辑**: AI产业链全景布局，高风险高收益
- **预期**: 收益20-30%，夏普0.8-1.0，风险高

#### **主线C: 中国资产重估**（政策驱动）
- **配置**: A股40% + 港股30% + 中国债券20% + 黄金10%
- **逻辑**: 政策驱动，估值修复+盈利增长
- **预期**: 收益15-25%，夏普0.9-1.1，风险中高

#### **对照组1: 等权重组合**
- **配置**: 6大类资产各16.67%
- **作用**: 被动基准，检验主动管理价值

#### **对照组2: 60/40股债组合**
- **配置**: 股票60% + 债券40%
- **作用**: 传统配置基准

### 2. 交易策略

| 策略 | 描述 | 特点 |
|------|------|------|
| **S1: Buy and Hold** | 买入持有 | 最简单，交易成本最低 |
| **S2: Monthly Rebalance** | 月度再平衡 | 定期调整至目标权重 |
| **S3: Quarterly Rebalance** | 季度再平衡 | 降低交易频率 |
| **S4: Dynamic Stop Loss** | 动态止损 | 月度再平衡+单资产-10%止损 |
| **S5: Risk Parity** | 风险平价 | 波动率加权，等风险贡献 |

### 3. 压力测试情景

| 情景 | 描述 | 冲击 |
|------|------|------|
| **情景1: 市场崩盘** | 股票资产下跌30% | 波动率×2 |
| **情景2: 利率冲击** | 利率上升200bp | 债券-14% |
| **情景3: 通胀飙升** | CPI上升5% | 商品+25%，股债下跌 |
| **情景4: 流动性危机** | 市场流动性枯竭 | 所有资产-20%，相关性→1 |
| **情景5: 历史重演** | 2008/2020危机 | 股票-35%，避险资产上涨 |

### 4. Brinson归因分析

分解组合超额收益来源：
- **配置效应**: 资产配置决策的贡献
- **选择效应**: 资产选择能力的贡献
- **交互效应**: 配置与选择的交互作用

---

## 📊 输出文件

### 数据文件（processed_data/）
- `returns_aligned.csv` - 对齐的收益率数据
- `prices_normalized.csv` - 标准化价格数据
- `summary_statistics.csv` - 统计摘要

### 分析结果（results/）
- `backtest_summary.csv` - 回测汇总（25个组合×策略）
- `correlation_report.txt` - 相关性分析报告
- `all_stress_tests.csv` - 所有压力测试结果
- `stress_report_[组合].txt` - 各组合压力测试报告
- `brinson_report_[组合].txt` - 各组合归因分析报告
- `[组合]_[策略]_value.csv` - 详细净值数据
- `[组合]_[策略]_weights.csv` - 权重历史数据

### 可视化图表（visualization/）

#### 相关性分析
- `correlation_heatmap.png` - 相关性热力图
- `rolling_correlation.png` - 滚动相关性曲线

#### 回测结果
- `portfolio_values.png` - 组合净值曲线
- `drawdown_comparison.png` - 回撤对比
- `monthly_returns_heatmap.png` - 月度收益热力图
- `rolling_metrics.png` - 滚动指标（收益、波动、夏普）

#### 绩效对比
- `all_portfolios_comparison.png` - 所有组合配置对比
- `performance_comparison_sharpe_ratio.png` - 夏普比率对比
- `performance_comparison_annualized_return.png` - 年化收益对比
- `efficient_frontier.png` - 有效前沿
- `risk_return_scatter.png` - 风险收益散点图
- `summary_dashboard.png` - 总览仪表板

#### 压力测试
- `stress_test_[组合].png` - 压力测试结果（每个组合）
- `stress_radar_[组合].png` - 压力测试雷达图

#### Brinson归因
- `brinson_waterfall_[组合].png` - 归因瀑布图
- `asset_attribution_[组合].png` - 资产级归因
- `attribution_pie_[组合].png` - 归因效应占比

**总计**: 20+ 张专业图表

---

## 🎨 配色方案

所有可视化使用统一的配色方案：

| 颜色 | 十六进制 | 用途 |
|------|---------|------|
| 淡紫罗兰 | #9B8FD9 | 主色调，环形图、柱状图 |
| 珊瑚红 | #E07A7A | 暖色强调，风险标识 |
| 薄荷绿 | #7AD0B0 | 冷色平衡，正收益 |
| 天空蓝 | #6BADEA | 信息色，连接线 |
| 暖橙色 | #F4A261 | 活力色，数据高亮 |
| 奶油黄 | #FCE49C | 辅助亮色，标注背景 |
| 灰蓝色 | #8FB9C7 | 沉稳辅助，次要信息 |
| 豆沙粉 | #D4A5A5 | 柔和过渡，细分色块 |

---

## 🔧 技术栈

- **Python 3.8+**
- **数据处理**: pandas, numpy
- **可视化**: matplotlib, seaborn, plotly
- **统计分析**: scipy, statsmodels
- **数据获取**: yfinance, akshare

---

## 📖 使用示例

### 示例1: 仅运行回测

```python
from backtesting_engine import PortfolioBacktester
from data_loader import DataLoader

# Load data
loader = DataLoader()
loader.load_all_assets()
returns_df = loader.align_data()
price_df = loader.get_price_data()

# Run backtest
backtester = PortfolioBacktester(initial_capital=1000000)
summary = backtester.run_full_backtest(config, price_df, returns_df)
print(summary.head())
```

### 示例2: 仅运行压力测试

```python
from stress_testing import StressTester

# Define portfolio
portfolio_weights = {'GOLD': 0.25, 'US_TECH': 0.25, 'HK_STOCK': 0.25, 'CN_BOND': 0.25}

# Run stress test
tester = StressTester(portfolio_weights, returns_df, price_df)
results = tester.run_all_scenarios()
tester.plot_stress_test_results(results)
```

### 示例3: 仅运行归因分析

```python
from brinson_attribution import BrinsonAttributor

# Define portfolios
portfolio_weights = {...}
benchmark_weights = {...}

# Run attribution
attributor = BrinsonAttributor(portfolio_weights, benchmark_weights, 
                               portfolio_returns, benchmark_returns, asset_returns)
results = attributor.calculate_brinson_attribution()
attributor.plot_attribution_waterfall()
```

---

## 📝 研究成果

### 已完成文档

1. **宏观研究报告**（8000字）
   - 全球经济格局分析
   - 货币政策周期研判
   - 地缘政治风险评估
   - 全球大类资产展望
   - 三条投资主线

2. **因子驱动矩阵**（4000字）
   - 9大宏观因子体系
   - 因子-资产影响矩阵
   - 2025年因子权重排序
   - 因子时变特征分析

3. **投资组合构建**（6000字）
   - 5个组合详细设计
   - 每个组合500字投资逻辑
   - 资产配置明细
   - 风险收益特征

### 待完成文档

4. **学术论文**（10页）
   - 整合所有研究成果
   - 包含所有图表和数据
   - 符合学术规范

---

## ⚠️ 注意事项

### 数据要求
1. CSV文件必须包含 `date` 列（YYYY-MM-DD格式）
2. 必须包含 `close` 或 `adj_close` 列
3. 不同资产的交易日可能不同，系统会自动对齐

### 常见问题

**Q: 如何修改组合权重？**  
A: 编辑 `portfolios_config.json` 文件中的 `assets` 字段

**Q: 如何添加新资产？**  
A: 
1. 将数据文件放入 `data/` 文件夹
2. 在 `portfolios_config.json` 的 `asset_mapping` 中添加配置
3. 在组合配置中添加权重

**Q: 回测运行时间长？**  
A: 5个组合×5个策略=25个回测，数据量大时可能需要5-10分钟

**Q: 如何只运行特定分析？**  
A: 使用 `main_analysis.py`（Phase 4-6）或直接调用相应模块

---

## 📞 项目信息

- **项目名称**: 现代投资组合分析系统
- **版本**: 1.0
- **创建日期**: 2024-12-31
- **最后更新**: 2026-05-05
- **完成度**: 90%（Phase 0-9完成，Phase 10待完成）

---

## 🎓 学术价值

本项目具有以下学术价值：

1. **系统性**: 完整的投资组合分析框架
2. **实用性**: 基于真实数据的回测验证
3. **创新性**: 多因子驱动+多策略对比
4. **规范性**: 符合学术研究标准
5. **可复现性**: 完整的代码和文档

---

## 📚 参考文献

主要理论基础：
- Modern Portfolio Theory (Markowitz, 1952)
- Brinson Attribution Model (Brinson, Hood & Beebower, 1986)
- Risk Parity (Qian, 2005)
- Factor Investing (Fama & French, 1993)

---

*最后更新: 2026-05-05*
