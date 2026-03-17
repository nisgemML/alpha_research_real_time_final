import numpy as np

def run_backtest(weights, returns, cost=0.001):
    positions = np.sign(weights)
    turnover = positions.diff().abs().sum(axis=1)
    pnl = positions.shift(1) * returns - turnover * cost
    return pnl, turnover
