from pwn import *
import numpy as np
import scipy as sp

NormalizeState = lambda state: state / sp.linalg.norm(state)

def NKron(*args):
  """Calculate a Kronecker product over a variable number of inputs"""
  result = np.array([[1.0]])
  for op in args:
    result = np.kron(result, op)
  return result

def qubit(a, b):
  return np.array([[a], [b]])

One  = qubit(0.0, 1.0)
Zero = qubit(1.0, 0.0)

ZeroZero = np.kron(Zero, Zero)
OneOne = np.kron(One, One)

P0 = np.dot(Zero, Zero.T)
P1 = np.dot(One, One.T)

Id = np.eye(2)
H = 1/np.sqrt(2) * np.array([[1.0, 1.0],
                             [1.0, -1.0]])

X = np.array([[0,1],
              [1,0]])

def measure(qb):
  CatState = NormalizeState(ZeroZero + OneOne)
  OuterProd = np.dot(qb, qb.T)
  #Find probability of measuring 0 on qubit 0
  Prob0 = np.trace(np.dot(NKron(P0, Id), OuterProd))

  #Simulate measurement of qubit 0
  if (np.random.rand() < Prob0):
    #Measured 0 on Qubit 0
    Result = 0
    ResultState = NormalizeState(np.dot(NKron(P0, Id), CatState))
  else:
    #Measured 1 on Qubit 1
    Result = 1
    ResultState = NormalizeState(np.dot(NKron(P1, Id), CatState))

  return Result, ResultState

def NH(n):
  return NKron(*[H for _ in range(n)])

def NKronBits(*args):
  if len(args) & 1 != 0:
    print("Noooo")
    return None

  else:
    qbs = [One if i == 1 else Zero for i in args]
    return NKron(*qbs)

def quantize(num, size):
  BitList = list(map(int, list(bin(num)[2:])))
  ExtraBits = [0] * (size - len(BitList))
  BitList = ExtraBits + BitList
  return NKronBits(*BitList)

# bitsize = int(input())
# inp = int(input())
# qin = quantize(4, 4)
# Had = NH(4)

# psi1 = np.dot(Had, qin)
# print(psi1)
# print("{:.12}".format(1/np.sqrt(2)))

# print(np.kron(np.kron(np.dot(H, Zero), np.dot(H, Zero)), np.kron(np.dot(H, Zero), np.dot(H, Zero))))
# print(np.dot(NH(4), np.kron(ZeroZero, ZeroZero)))
context.log_level = 'error'
flag = ""
to_send = []
for i in range(7, -1, -1):
	if (0 >> i) & 1 == 1:
		t = np.dot(H, One)
	else:
		t = np.dot(H, Zero)
	to_send.append(t[0][0])
	to_send.append(t[1][0])

for i in range(len(to_send)):
	to_send[i] = "{:.12}".format(to_send[i]).encode()

for ind in range(35):
  r = remote("localhost", 9696)

  payload = b" ".join(to_send)

  r.recvuntil(b": ")
  r.sendline(str(ind).encode())
  try:
    r.recvuntil(b": ")
  except:
    break
  r.sendline(payload)
  flag += chr(int(r.recvline().decode()))
  print(flag)
  r.close()

print(flag)

