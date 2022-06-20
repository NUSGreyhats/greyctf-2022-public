from pwn import *
from secrets import randbits

r = remote("localhost", 5555)

n = 3
bits = 64

arr = [randbits(399) for i in range(n * 2)]

payload = ''

for i in range(0, len(arr), 2):
    payload += f'{arr[i]} {arr[i + 1]},'

payload = payload[:-1]    

r.sendline(payload)
r.recvuntil('Re(<v1, v2>) = ').decode()
p = int(r.recvline().strip())
mat = []
for i in range(n * 2):
    row = [0 for i in range(n * 2 + 2)]
    row[i] = 1
    row[-2] = -arr[i]
    mat.append(row)

mat.append([0 for i in range(n * 2)] + [p, 2^bits])

M = Matrix(mat)

ans = list(M.LLL()[0])

payload = ''

for i in range(0, len(arr), 2):
    payload += f'{ans[i]} {ans[i + 1]},'

payload = payload[:-1]    

r.sendline(payload)
r.interactive()
