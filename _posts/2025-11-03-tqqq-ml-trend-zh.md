---
title: 'TQQQ ML 趋势：用机器学习预测 3 倍杠杆 ETF'
date: 2025-11-03
permalink: /zh/posts/2025/11/tqqq-ml-trend/
tags:
  - tqqq
  - machine-learning
  - quantitative-finance
  - leveraged-etf
  - python
  - trading
  - time-series
---
TQQQ 是纳斯达克 100 指数的 3 倍杠杆 ETF。它也是散户接触过的最不对称的金融工具之一——上行空间真实存在，回撤却十分残酷，而每日再平衡的数学逻辑意味着"买入并持有"并不像大多数人以为的那样运转。TQQQ ML Trend 是一个用机器学习来预测趋势状态的实验，而不是去预测价格。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

[![GitHub stars](https://img.shields.io/github/stars/ktwu01/TQQQ-ML-trend?style=social)](https://github.com/ktwu01/TQQQ-ML-trend/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ktwu01/TQQQ-ML-trend?style=social)](https://github.com/ktwu01/TQQQ-ML-trend/fork)

## 为什么偏偏选 TQQQ

TQQQ 之所以有趣，是因为在来回震荡的行情中，杠杆衰减惩罚很严重，而在趋势行情中，凸性又极其可观。这种不对称，正是机器学习原则上能学会的那类状态——即使它无法可靠地预测逐日的价格。

假设是：一个把"我们是不是处于趋势行情"分类出来的模型，比一个试图预测明日收益率的模型更有用。

## 这个仓库包含什么

- 用于历史纳斯达克 100 和 TQQQ 价格序列的**数据摄入**。
- 专注于波动率、动量和广度的**特征工程**。
- 使用标准机器学习库来进行趋势状态分类的**模型训练**。
- 尊重真实交易成本和滑点的**回测框架**。
- 样本内与样本外表现的**可视化**。

## 如何运行

```bash
git clone https://github.com/ktwu01/TQQQ-ML-trend.git
cd TQQQ-ML-trend
pip install -r requirements.txt
python main.py
```

## 技术栈

- **Python** 处理一切。
- 标准的数据和机器学习库（pandas、scikit-learn 等）。
- 回测逻辑从零手写，以避免隐式的假设。

## 关于现实的一点说明

这是研究代码，不是交易系统。回测容易受到前视偏差、状态过拟合和幸存者偏差的影响。请把这个仓库当作你自己分析的起点，而不是投资建议。即使市场最终会恢复，杠杆 ETF 也可能迅速贬值。

## 使用场景

- 学习如何搭建一个由机器学习驱动的回测。
- 作为金融时间序列特征工程的参考。
- 作为你自己状态分类工作的起点。

## 参与贡献

如果你有关于更优特征、更诚实的验证方案或替代模型的想法，欢迎在 [github.com/ktwu01/TQQQ-ML-trend](https://github.com/ktwu01/TQQQ-ML-trend) 提交 issue 或 PR。

---

杠杆 ETF 研究有趣的地方，不在于杠杆本身。而在于杠杆迫使你去直面自己模型的那些假设。