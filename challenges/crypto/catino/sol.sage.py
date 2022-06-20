

# This file was *autogenerated* from the file sol.sage
from sage.all_cmdline import *   # import sage library

_sage_const_8000 = Integer(8000); _sage_const_4 = Integer(4); _sage_const_2048 = Integer(2048); _sage_const_100 = Integer(100); _sage_const_4900 = Integer(4900); _sage_const_10 = Integer(10); _sage_const_50365 = Integer(50365); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_5000 = Integer(5000)
from pwn import *
from decimal import Decimal, getcontext

getcontext().prec = int(_sage_const_8000 )

r = remote("localhost", "4000")

power = _sage_const_4 

size = _sage_const_2048 
ind = _sage_const_100 
indBit = int(ind).bit_length()

given = ''

for i in range(_sage_const_4900 ):
    r.sendline("0")
    r.recvuntil("it was ")
    given += r.recvline().strip().decode()

length = len(given)
a = int(given)
pad = _sage_const_10 **length
bit = int(pad).bit_length()

# cc = bit
# dd = int((q * pad + a)^power - int(n) * pad^power).bit_length()
# print(dd)

dd = _sage_const_50365 

M = []

for i in range(power + _sage_const_1 ):
    row = [_sage_const_0  for i in range(power * _sage_const_2  + _sage_const_3 )]
    row[i] = _sage_const_1 
    if (i != _sage_const_0 ):
        row[i + power + _sage_const_2 ] = _sage_const_2 **(dd - (size + indBit) * (power - i))
    else:
        row[i + power + _sage_const_2 ] = _sage_const_2 **(dd - (size + indBit))
    
    row[power + _sage_const_1 ] = binomial(power, i) * a**i * pad**(power - i)
    M.append(row)

M = Matrix(ZZ, M)
ans = str(M.LLL()[_sage_const_0 ][power - _sage_const_1 ])

n = int(Decimal(ans[:-ind] + "." + ans[-ind:] + given) ** power) + _sage_const_1 
n = Decimal(int(n))
p = Decimal(float(_sage_const_1 /_sage_const_4 ))
k = str(n**p).split('.')[_sage_const_1 ][_sage_const_5000 :]

for i in range(_sage_const_100 ):
    r.sendline(k[i])

r.interactive()

