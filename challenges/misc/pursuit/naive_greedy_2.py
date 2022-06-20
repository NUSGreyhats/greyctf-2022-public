import sys
from decimal import *
from pwn import *
import numpy as np
getcontext().prec = 300
graph = []

r = remote("localhost", 6969)

r.recvlines(numlines=2)

def guess(k:int) -> str:
	r.sendlineafter(b">", str(k).encode())
	return r.recvline(keepends=False).decode()

def choose_start(graph) -> int:
	f = np.array([Decimal(0) for _ in range(len(graph))])
	for u in range(len(graph)):
		for v, p in graph[u]:
			f[v] += 1/Decimal(N) * Decimal(p)
	return int(np.argmax(f))

def update_prob(prob, g):
	new_prob = np.array([Decimal(0) for _ in range(len(prob))])
	for u in range(len(graph)):
		total_pr = Decimal(0)
		for v, p in graph[u]:
			if v == g: continue
			total_pr += Decimal(p)

		for v, p in graph[u]:
			if v == g: continue
			new_prob[v] += prob[u] * Decimal(p) / total_pr

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
	g = choose_start(graph)
	resp = guess(g)
	gc += 1
	arr = [0, 0]
	with log.progress("Guessing...") as p:
		while True:
			if gc < 10:
				prob = update_prob(prob, g)
				g = int(np.argmax(prob))
				arr[gc & 1] = g
				p.status("%s %s" % (str(g), str(prob[g])))

				resp = guess(g)
			else:
				resp = guess(arr[gc & 1])
				p.status("%s %s" % (str(g), str(prob[g])))
			gc += 1

			if "Nope" not in resp:
				if "lose" in resp: p.success("lost")
				else: p.success(str(gc))
				break
	
