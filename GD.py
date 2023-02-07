import time
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2 - 5*x + 5


def df(x):
    return 2*x - 5

N = 20
xx = 0
lmd = 0.1

x_plt = np.arange(0, 5.0, 0.1)

print(x_plt)