from numpy import random as nrandom
from random import randint, random
from math import sqrt

def rand(start, end) -> float:
  return random() * (end - start) + start

count = 3
interval = [-30, 30]

means = [-12.325308285692675, 1.9802198205222012, 15.143309061102336]
variance = 1
sigma = round(sqrt(variance))
means.sort()
print(means)

def sample(mu, sigma):
    return nrandom.normal(mu, sigma)

points = []
for _ in range(800):
    mean = means[randint(0, len(means)-1)]
    points.append(sample(mean, sigma))

with open("data.txt", "w") as f:
    inter = list(map(str,interval))
    ps = list(map(str, points))

    f.writelines([
      f"num_of_mean = {count}\n",
      f"variances = {variance}\n",
      f"interval = [{', '.join(inter)}]\n",
      f"data = [{', '.join(ps)}]\n"
    ])

