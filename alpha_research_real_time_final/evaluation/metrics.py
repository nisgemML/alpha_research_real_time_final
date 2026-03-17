import numpy as np
from scipy import stats

def sharpe(returns):
    return np.sqrt(252) * returns.mean() / returns.std()

def max_drawdown(cum_returns):
    peak = cum_returns.cummax()
    drawdown = (cum_returns - peak) / peak
    return drawdown.min()

def t_test(returns):
    return stats.ttest_1samp(returns, 0)
