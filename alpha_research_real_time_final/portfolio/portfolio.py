def long_short_portfolio(signals, top_k=1):
    ranks = signals.rank(axis=1)
    long = ranks >= (ranks.shape[1] - top_k)
    short = ranks <= top_k
    weights = long.astype(int) - short.astype(int)
    weights = weights.div(weights.abs().sum(axis=1), axis=0)
    return weights
