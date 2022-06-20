#!/usr/bin/python3
import numpy as np

g0 = np.array([1,1,1])
g1 = np.array([1,0,1])

flag = <REDACTED>

def str_to_bits(s):
	res = []
	for c in s:
		b = ord(c)
		res += [(b >> i) & 1 for i in range(8)]

	return res

def encode(bits):
	shift_regs = [0, 0]
	output = []

	for bit in bits:
		current_state = np.array([bit] + shift_regs)

		p0 = np.sum(current_state * g0) & 1
		p1 = np.sum(current_state * g1) & 1

		output += [p0, p1]

		shift_regs = [bit, shift_regs[0]]

	return output

def encode_str(s):
	bits = str_to_bits(s)
	return encode(bits)

noise_rate = 0.015
def add_noise(bits):
	for i in range(len(bits)):
		if np.random.random_sample() < noise_rate:
			bits[i] ^= 1
	return bits

flag_data = encode_str(flag)
data = add_noise(flag_data)
print("A secret message flies across the sky, but it's a little noisy so I can't understand...")
print("".join(list(map(str, data))))
