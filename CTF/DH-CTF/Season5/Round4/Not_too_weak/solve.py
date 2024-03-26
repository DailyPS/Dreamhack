import sys
from pwn import *

PROB_PATH = './prob.py'
if len(sys.argv) == 3:
    p = remote(sys.argv[1], int(sys.argv[2]))
else:
    p = process(PROB_PATH)

p.sendlineafter(b'> ', b'2')
p.sendlineafter(b'> ', b'01fe01fe01fe01fe')
p.recvuntil(b'> ')
encflag = p.recvline(keepends=False)

print(encflag)

p.sendlineafter(b'> ', b'1')
p.sendlineafter(b'> ', b'fe01fe01fe01fe01')
p.sendlineafter(b'> ', encflag)
p.recvuntil(b'> ')
flag = p.recvline(keepends=False).decode()

print(bytes.fromhex(flag))