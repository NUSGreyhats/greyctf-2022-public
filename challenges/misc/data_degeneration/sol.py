from scipy.stats import norm
from random import random
from decimal import *
from tqdm import tqdm

def rand(start, end) -> float:
  return random() * (end - start) + start

count = 3
interval = [-30, 30]
sigma = 1
data = list(map(float, open("test.txt", "r").read().split(", ")))
print(len(data))

h = []
def solve(X, delta):
    def norm_pdf(mu, sigma, x):
        return Decimal(norm(mu, sigma).pdf(x))

    def E(d, m):
        global h
        denom = Decimal(0)
        for mu in h:
            denom += norm_pdf(mu, sigma, X[d])
        return norm_pdf(h[m], sigma, X[d]) / denom

    def step():
        global h
        next_h = [0.0 for _ in range(len(h))]
        # for i in tqdm(range(len(h))):
        for i in range(len(h)):
            numer = Decimal(0)
            denom = Decimal(0)
            for d in range(len(X)):
                e = E(d, i)
                numer += e * Decimal(X[d])
                denom += e
                
            next_h[i] = float(numer / denom)
            
        stop = True
        for a, b in zip(h, next_h):
            if abs(a - b) >= delta:
                stop = False

        h = next_h

        return stop

    # print("Start!")
    # iteration = 1
    stop = False
    while not stop:
      # print("iteration %d" % iteration)
      # iteration += 1
      # print(sorted(h))
      stop = step()
      
    h.sort()
    print(h)


for i in range(5):
    h = [rand(*interval) for _ in range(count)]
    solve(data, 0.1)

