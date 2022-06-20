#!/usr/bin/python3

from qiskit import BasicAer
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
import numpy as np
import scipy as sp
import scipy.linalg
import sys

NormalizeState = lambda state: state / sp.linalg.norm(state)

def NKron(*args):
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
  Prob0 = np.trace(np.dot(P0, OuterProd))

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

def GetIndex(lst):
	lst = list(map(float, lst))
	res = 0
	for i in range(0, len(lst), 2):
		q = np.resize(lst[i:i+2], (2,1))
		p, _ = measure(np.dot(H, q))
		if p == 1:
			res += 1 << (i >> 1)

	return res

print("QFC 6000, the ultimate geeky machinery that works like magic")

N = 8
flag = "grey{Qu4nTuM_I5_S0_sC4Ry}"

index = int(input("Flag index: "))
if index >= len(flag):
	print("Flag isn't this long. A quantum machine can't check something that doesn't exist.")
	sys.exit(0)

guess = list(map(float, input("Qubyte: ").split(" ")))
if len(guess) != 2 * N:
	print("You need 16 numbers to represent a qubyte")
	sys.exit(0)

# index = GetIndex(guess)
try:
  a = ord(flag[index])  # integer in the oracle function f

  qr = QuantumRegister(N)  # Initialize qubits
  cr = ClassicalRegister(N)  # Initialize bits for record measurements
  circuit = QuantumCircuit(qr, cr)

  for i in range(0, len(guess), 2):
    b = guess[i:i+2]
    circuit.initialize(b, i // 2)

except:
  print(np.random.randint(0, 255))
  sys.exit(0)
# circuit.x(qr[n])  # initialize the ancilla qubit in the |1> state

circuit.barrier()

# First step of quantum algorithms - Prepare the superposition
# For superposition, we apply the Hadamard gate on all qubits
# circuit.h(qr)

circuit.barrier()

# Oracle function
for i in range(N):
    if (a & (1 << i)):
        circuit.z(qr[i])
    else:
        circuit.id(qr[i])

circuit.barrier()

# Apply Hadamard gates after querying oracle function
circuit.h(qr)

circuit.barrier()

# Measure qubits
for i in range(N):
    circuit.measure(qr[i], cr[i])

# print(circuit.draw())

# Run our circuit with local simulator
backend = BasicAer.get_backend('qasm_simulator')
shots = 5000
results = execute(circuit, backend=backend, shots=shots).result()

answer = results.get_counts()
key = []
val = []
for k, v in answer.items():
	key.append(k)
	val.append(v)
print(int(key[np.argmax(val)], 2))
sys.exit(0)
