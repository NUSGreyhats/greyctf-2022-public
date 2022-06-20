from pwn import *

r = remote("localhost", 4000, level='debug')

r.sendline("1")
r.sendline("0")
r.recvuntil("go! ")
n = int(r.recvline())
f = factor(n)

for i in f:
    r.sendline("2")
    r.sendline(str(i[0]))

r.recvall()

# grey{The_Answer_To_The_Riddle_Is_"Road"!_ZvBtTpyA4GXuuwjB}