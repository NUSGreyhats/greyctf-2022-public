

# This file was *autogenerated* from the file sol.sage
from sage.all_cmdline import *   # import sage library

_sage_const_4000 = Integer(4000); _sage_const_0 = Integer(0)
from pwn import *

r = remote("localhost", _sage_const_4000 , level='debug')

r.sendline("1")
r.sendline("0")
r.recvuntil("go! ")
n = int(r.recvline())
f = factor(n)

for i in f:
    r.sendline("2")
    r.sendline(str(i[_sage_const_0 ]))

r.recvall()

