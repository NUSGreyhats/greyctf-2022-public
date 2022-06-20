from secrets import randbits
from decimal import Decimal, getcontext

getcontext().prec = int(6000)

power = 4

size = 2048
ind = 100
indBit = int(ind).bit_length()

n = Decimal(randbits(size))
p = Decimal(float(1/power))
k = str(n^p)

i = k.find('.')
t = k.replace('.', '')
q = int(t[:i + ind])
a = t[i + ind: i + ind + 4900]

length = len(a)
a = int(a)
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
print(M.LLL()[0][power - 1])
print(k)
