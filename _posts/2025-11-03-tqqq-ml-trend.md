---
title: 'TQQQ ML Trend: Predicting a 3x Leveraged ETF With Machine Learning'
date: 2025-11-03
permalink: /posts/2025/11/tqqq-ml-trend/
tags:
  - tqqq
  - machine-learning
  - quantitative-finance
  - leveraged-etf
  - python
  - trading
  - time-series
---
TQQQ is the 3x-leveraged Nasdaq-100 ETF. It is also one of the most asymmetric instruments retail investors touch — the upside is real, the drawdowns are brutal, and the daily-rebalance math means buy-and-hold doesn't behave the way most people assume. TQQQ ML Trend is an experiment in using machine learning to predict the trend regime, not the price.

> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); [GitHub: ktwu01](https://github.com/ktwu01/)

[![GitHub stars](https://img.shields.io/github/stars/ktwu01/TQQQ-ML-trend?style=social)](https://github.com/ktwu01/TQQQ-ML-trend/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ktwu01/TQQQ-ML-trend?style=social)](https://github.com/ktwu01/TQQQ-ML-trend/fork)

## Why TQQQ Specifically

TQQQ is interesting because the leverage decay penalty in choppy markets is severe and the convexity in trending markets is enormous. That asymmetry is exactly the kind of regime ML can, in principle, learn — even if it cannot reliably predict day-to-day prices.

The hypothesis: a model that classifies "are we in a trending regime or not" is more useful than one that tries to predict tomorrow's return.

## What This Repo Contains

- **Data ingestion** for historical Nasdaq-100 and TQQQ price series.
- **Feature engineering** focused on volatility, momentum, and breadth.
- **Model training** using standard ML libraries to classify trend regimes.
- **Backtest framework** that respects realistic transaction costs and slippage.
- **Visualizations** of in-sample vs. out-of-sample performance.

## How to Run

```bash
git clone https://github.com/ktwu01/TQQQ-ML-trend.git
cd TQQQ-ML-trend
pip install -r requirements.txt
python main.py
```

## Tech Stack

- **Python** for everything.
- Standard data and ML libraries (pandas, scikit-learn, etc.).
- Backtest logic implemented from scratch to avoid silent assumptions.

## A Note on Reality

This is research code, not a trading system. Backtests are vulnerable to look-ahead bias, regime overfitting, and survivorship bias. Treat the repo as a starting point for your own analysis, not as financial advice. Leveraged ETFs can lose value rapidly even in markets that eventually recover.

## Use Cases

- Learning how to structure an ML-driven backtest.
- A reference for feature engineering on financial time series.
- A starting point for your own regime-classification work.

## Contributing

If you have ideas for better features, more honest validation schemes, or alternative models, open an issue or PR at [github.com/ktwu01/TQQQ-ML-trend](https://github.com/ktwu01/TQQQ-ML-trend).

---

The interesting part of leveraged ETF research is not the leverage. It is what the leverage forces you to confront about your own model's assumptions.
