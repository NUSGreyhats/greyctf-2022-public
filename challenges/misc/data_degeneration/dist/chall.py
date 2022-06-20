import numpy as np
import random as r
from math import sqrt
import time

r.seed(time.time())

def rand(start, end) -> float:
  return r.random() * (end - start) + start

count = 3
interval = [-30, 30]

means = [rand(*interval) for _ in range(count)]
variance = 1
std_dev = round(sqrt(variance))

def sample(mu, sigma):
    return np.random.normal(mu, sigma)

points = []
for _ in range(800):
    mean = means[r.randint(0, len(means)-1)]
    points.append(sample(mean, std_dev))

with open("data.txt", "w") as f:
    inter = list(map(str,interval))
    ps = list(map(str, points))

    f.write(", ".join(ps))

