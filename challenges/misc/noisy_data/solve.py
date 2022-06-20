import numpy as np
from pwn import *

g0 = np.array([1,1,1])
g1 = np.array([1,0,1])

def decode(bits):
	if len(bits) % 8 != 0:
		print("Cannot encode bits")
		return ""

	msg = ""
	for i in range(0, len(bits), 8):
		byte = bits[i:i+8]
		ch = 0
		for i in range(8):
			ch += byte[i] << i
		msg += chr(ch)

	return msg

def naive_decode(bits):
	shift_regs = [0, 0]
	output = []

	for i in range(0, len(bits), 2):
		a, b = bits[i:i+2]

		bit = -1
		for tmp in [0, 1]:
			current_state = [tmp] + shift_regs
			p0 = np.sum(current_state * g0) & 1
			p1 = np.sum(current_state * g1) & 1
			if p0 == a and p1 == b:
				bit = tmp

		if bit == -1:
			print("Cannot decode this message")
			return []

		output += [bit]

		shift_regs = [bit, shift_regs[0]]

	return output

bit_count = dict([(0, 0), (1, 1), (2, 1), (3, 2)])

path_metric = [
    [0, -1, 3, -1],
    [3, -1, 0, -1],
    [-1, 1, -1, 2],
    [-1, 2, -1, 1]]

def hamming_dist(a, b):
  if a < 0 or b < 0: return 0
  return abs(bit_count[a] - bit_count[b])

noise_rate = 0.012
def entropy(dist):
  return (1 - noise_rate)**(2-dist) * noise_rate**dist

def emission_prob(start):
  return np.array([[entropy(hamming_dist(j, path_metric[start][i])) for j in range(4)] for i in range(4)])

def viterbi(y, A, Pi=None):
    # Cardinality of the state space
    K = A.shape[0]
    # Initialize the priors with default (uniform dist) if not given by caller
    Pi = Pi if Pi is not None else np.full(K, 1 / K)
    T = len(y)
    T1 = np.empty((K, T), 'd')
    T2 = np.empty((K, T), 'B')

    # Initilaize the tracking tables from first observation
    T1[:, 0] = Pi
    T2[:, 0] = 0

    # Iterate throught the observations updating the tracking tables
    for j in range(1, T):
      for i in range(K):
        T1[i, j] = np.max([T1[k, j - 1] * A[k, i] * emission_prob(k)[i, y[j]] for k in range(K)])
        T2[i, j] = np.argmax([T1[k, j - 1] * A[k, i] for k in range(K)])

    # Build the output, optimal model trajectory
    x = np.empty(T, 'B')
    x[-1] = np.argmax(T1[:, T - 1])
    for i in reversed(range(1, T)):
        x[i - 1] = T2[x[i], i]

    return x, T1, T2

def process(data):
	result = []
	for i in range(0,len(data),2):
		a, b = data[i:i+2]
		result.append(b * 2 + a)
	return result

r = remote("localhost", 6969)
print(r.recvline())
data = list(map(int, list(r.recvline(keepends=False).decode())))
data = process(data)
path, _, __ = viterbi(
	data,
	np.array([
		[0.5, 0, 0.5, 0],
		[0.5, 0, 0.5, 0],
		[0, 0.5, 0, 0.5],
		[0, 0.5, 0, 0.5]]),
	np.array([1, 0, 0, 0])
)

print(decode([1] + [i >> 1 for i in path[1:]]))

