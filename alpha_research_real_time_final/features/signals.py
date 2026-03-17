import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA

def momentum(prices, window=5):
    return prices.pct_change(window)

def mean_reversion(prices, window=10):
    return -(prices - prices.rolling(window).mean()) / prices.rolling(window).std()

def cross_sectional_rank(prices):
    return prices.rank(axis=1)

def residual_signal(prices, market):
    residuals = pd.DataFrame(index=prices.index, columns=prices.columns)
    for t in prices.index:
        y = prices.loc[t].values.reshape(-1,1)
        X = market.loc[t].values.reshape(-1,1)
        model = LinearRegression().fit(X, y)
        residuals.loc[t] = (y - model.predict(X)).flatten()
    return residuals

def pca_factors(prices, n_components=2):
    pca = PCA(n_components=n_components)
    factors = pca.fit_transform(prices.fillna(0))
    return pd.DataFrame(factors, index=prices.index, columns=[f'PCA_{i+1}' for i in range(n_components)])
