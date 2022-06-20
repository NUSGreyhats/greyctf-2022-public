import sys
from decimal import *
from pwn import *
import numpy as np
getcontext().prec = 100
graph = []

r = remote("localhost", 6969)

r.recvlines(numlines=2)

def guess(k:int) -> str:
	r.sendlineafter(b">", str(k).encode())
	return r.recvline(keepends=False).decode()

def update_prob(prob, g):
	# prob = prob / float(np.sum(prob)) # normalize
	new_prob = np.array([Decimal(0) for _ in range(len(prob))])
	prior = np.array([Decimal(0) for _ in range(len(prob))])
	for u in range(len(graph)):
		for v, p in graph[u]:
			prior[v] += prob[u] * Decimal(p)

	for u in range(len(prob)):
		pr = Decimal(0)
		for v, p in graph[g]:
			# g -> u
			if v == u: pr = Decimal(p)

		"""
		P(u[t] | not g[t-1]) = P(not g[t-1] | u[t]) * P(u[t]) / P(not g[t-1])
		where
		P(not g[t-1] | u[t])
		= 1 - ratio of weighted g->u prob to total weighted sum, if g->u exists
		= 1, otherwise
		P(u[t]) = weighted sum of incoming node with edges, i.e. prior
		P(not g[t-1]) = 1 - P(not g[t-1])
		"""

		if prior[u] == 0:
			new_prob[u] = 0
			continue
		marginal = Decimal(1) - pr * prob[g] / prior[u]
		model = Decimal(1) - prob[g]
		new_prob[u] = prior[u] * marginal / model

	# print(np.sum(new_prob))
	# if np.sum(new_prob) == 0:
	# 	new_prob = np.array([Decimal(1)/Decimal(N) for _ in range(N)])
	new_prob = new_prob / np.sum(new_prob)
	return new_prob

### SHOULD PLAY 3 ROUNDS
while True:
	tN= r.recvline(keepends=False).decode()
	try:
		N = int(tN)
		n = int(r.recvline(keepends=False).decode())
	except:
		print(tN)
		sys.exit(0)
	graph = [[] for _ in range(N)]

	for i in range(n):
		u, v, w = r.recvline(keepends=False).decode().split(" ")
		u, v = int(u), int(v)
		w = float(w)

		graph[u].append((v, w))

	print(N, n)
	prob = np.array([Decimal(1)/Decimal(N) for _ in range(N)])
	gc = 0
	with log.progress("Guessing...") as p:
		while True:
			g = int(np.argmax(prob))
			if prob[g] < Decimal(0.0045):
				g = np.random.choice(list(range(N)), p=np.array(prob, dtype="float64"))
			p.status(str(prob[g]))

			resp = guess(g)
			gc += 1

			if "Nope" not in resp:
				if "lose" in resp: p.success("lost")
				else: p.success(str(gc))
				break

			prob = update_prob(prob, g)
	
