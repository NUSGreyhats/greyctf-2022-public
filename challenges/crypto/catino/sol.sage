from pwn import *
from decimal import Decimal, getcontext

getcontext().prec = int(8000)

r = remote("localhost", "4000")

power = 4

size = 2048
ind = 100
indBit = int(ind).bit_length()

given = ''

for i in range(4900):
    r.sendline("0")
    r.recvuntil("it was ")
    given += r.recvline().strip().decode()

length = len(given)
a = int(given)
pad = 10^length
bit = int(pad).bit_length()

# cc = bit
# dd = int((q * pad + a)^power - int(n) * pad^power).bit_length()
# print(dd)

dd = 50365

M = []

for i in range(power + 1):
    row = [0 for i in range(power * 2 + 3)]
    row[i] = 1
    if (i != 0):
        row[i + power + 2] = 2^(dd - (size + indBit) * (power - i))
    else:
        row[i + power + 2] = 2^(dd - (size + indBit))
    
    row[power + 1] = binomial(power, i) * a^i * pad^(power - i)
    M.append(row)

M = Matrix(ZZ, M)
ans = str(M.LLL()[0][power - 1])

n = int(Decimal(ans[:-ind] + "." + ans[-ind:] + given) ^ power) + 1
n = Decimal(int(n))
p = Decimal(float(1/4))
k = str(n^p).split('.')[1][5000:]

for i in range(100):
    r.sendline(k[i])

r.interactive()
