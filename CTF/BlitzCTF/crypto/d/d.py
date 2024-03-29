from Crypto.Util.number import *
from flag import flag

p = bytes_to_long(flag)
assert isPrime(p)
q = getPrime(256) # 256 bit prime
d = pow(65537, -1, (p - 1) * (q - 1))
print(d)
# 22800184635336356769510601710348610828272762269559262549105379768650621669527077640437441133467920490241918976205665073