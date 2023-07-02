### > https://tutorials.pytorch.kr/beginner/nn_tutorial.html
from pathlib import Path
import requests
import pickle
import gzip
from matplotlib import pyplot
import numpy as np
import torch
from torch import nn
import torch.nn.functional as F
import math


DATA_PATH = Path("data")
PATH = DATA_PATH / "mnist"
PATH.mkdir(parents = True, exist_ok= True)
URL = "https://github.com/pytorch/tutorials/raw/main/_static/"
FILENAME = "mnist.pkl.gz" # python format
if not (PATH / FILENAME).exists():
    content = requests.get(URL + FILENAME).content
    (PATH / FILENAME).open("wb").write(content)
with gzip.open((PATH / FILENAME).as_posix(), "rb") as f:
    ((x_train, y_train), (x_valid, y_valid), _) = pickle.load(f, encoding="latin-1")
    
        
pyplot.imshow(x_train[0].reshape((28, 28)), cmap = "gray")
print(x_train.shape)
x_train, y_train, x_valid, y_valid = map(torch.tensor, (x_train, y_train, x_valid, y_valid))
n, c = x_train.shape
print(x_train, y_train)
print(x_train.shape)
print(y_train.min(), y_train.max())

########## method 1
weights = torch.randn(784, 10) / math.sqrt(784)
weights.requires_grad_()
bias = torch.zeros(10, requires_grad= True)
def log_softmax(x):
    return x - x.exp().sum(-1).log().unsqueeze(-1) # ? -1 
def model(xb):
    return log_softmax(xb @ weights + bias)
bs = 64
xb = x_train[0:bs] # mini-batch
preds = model(xb)
preds[0], preds.shape
print(preds[0], preds.shape) 
'''
preds[0] 
>>> tensor([-2.1382, -2.2753, -2.1900, -2.5995, -2.4144, -2.6447, -2.2098, -2.1514,
        -2.4306, -2.1315], grad_fn=<SelectBackward0>)
'''
def nll(input, target):
    return -input[range(target.shape[0]), target].mean() # ? 
loss_func = nll
yb = y_train[0:bs]
print(loss_func(preds, yb)) # ? tensor(0.0819, grad_fn=<NegBackward0>) tensor(1.)

##### method 2
loss_func = F.cross_entropy
def model(xb):
    return xb @ weights + bias
print(loss_func(model(xb), yb), accuracy(model(xb), yb)) # ? accuracy
############################################################

class Mnist_Logistic(nn.Module):
    def __init__(self):
        super().__init__()
        self.weights = nn.Parameter(torch.randn(784, 10) / math.sqrt(784))
        self.bias = nn.Parameter(torch.zeros(10))
    def forward(self, xb):
        return xb @ self.weights + self.bias
    
model = Mnist_Logistic()
print(loss_func(model(xb), yb))

    
### old version
# with torch.no_grad():
#     weights -= weights.grad * lr # ? lr
#     bias -= bias.grad * lr # ? lr
#     weights.grad.zero_() # grad.
#     bias.grad.zero_() # grad.
### new version
# with torch.no_grad():
#     for p in model.parameters(): p -= p.grad * lr # ? lr
#     model.zero_grad()

def fit():
    for epoch in range(epochs): # ? epochs
        for i in range((n-1) // bs + 1):
            start_i = i * bs
            end_i = start_i + bs
            xb = x_train[start_i:end_i]
            yb = y_train[start_i:end_i]
            pred = model(xb)
            loss = loss_func(pred, yb)
            
            loss.backward()
            with torch.no_grad():
                for p in model.parameters():
                    p -= p.grad * lr # ? lr
                model.zero_grad()
fit()
    