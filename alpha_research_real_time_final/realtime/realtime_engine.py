import time
import numpy as np

class RealTimeEngine:
    def __init__(self):
        self.prices_window = []

    def update(self, price_tick):
        self.prices_window.append(price_tick)
        if len(self.prices_window) > 50:
            self.prices_window.pop(0)

    def compute_signal(self):
        if len(self.prices_window) < 10:
            return 0
        arr = np.array(self.prices_window)
        return (arr[-1] - arr.mean()) / arr.std()
