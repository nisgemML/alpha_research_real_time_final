import pandas as pd
from data.loader import load_data
from features.signals import momentum, mean_reversion, cross_sectional_rank, residual_signal, pca_factors
from portfolio.portfolio import long_short_portfolio
from backtest.engine import run_backtest
from evaluation.metrics import sharpe, max_drawdown, t_test

# Load data
prices = load_data("data/prices.csv")
returns = prices.pct_change().fillna(0)

# Signals
mom = momentum(prices)
mr = mean_reversion(prices)
cs = cross_sectional_rank(prices)
resid = residual_signal(prices, prices.mean(axis=1))
pca = pca_factors(prices)

signals = (mom + mr + cs + resid)/4

# Portfolio
weights = long_short_portfolio(signals)

# Backtest
pnl, turnover = run_backtest(weights, returns)
cum_pnl = pnl.cumsum()

print("Sharpe:", sharpe(pnl.mean(axis=1)))
print("Max Drawdown:", max_drawdown(cum_pnl.mean(axis=1)))
print("t-test:", t_test(pnl.mean(axis=1)))

cum_pnl.mean(axis=1).to_csv("data/cum_pnl.csv")
