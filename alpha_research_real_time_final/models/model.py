from sklearn.linear_model import Ridge
import torch
import torch.nn as nn

def train_linear(X, y):
    model = Ridge()
    model.fit(X, y)
    return model

class AlphaMLModel(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )

    def forward(self, x):
        return self.net(x)
