from Crypto.Util.number import *

one_minus_ed = 1494255700446038813603416304291116907852512020860105389680719273898055792355796087321348579564087105168984643943590671889200

factorized = [(2, 4), (3, 1), (5, 2), (37, 1), (1117, 1), (4029461, 1), (1403014978139, 1), (284368748316481195117, 1), (18741210882440665187461519398960291465361283084482741278982029639876282810203, 1)]
all_factor = [1] # factors of ed - 1

for (base, expo) in factorized:
  factors = list()
  
  for factor in all_factor:
    for i in range(1, expo + 1):
      factors.append(factor * (base ** i))
  
  all_factor += factors
  
for factor in all_factor:
  num = factor + 1
  
  if isPrime(num):
    num_bytes = long_to_bytes(num)
    if b'DH{' in num_bytes:
      print("FLAG : {}".format(num_bytes.decode('utf-8')))
      print("p : {}".format(num))
      print("h : {}".format(one_minus_ed / num))
    elif num.bit_length() == 256:
      print("q : {}".format(num))
      print("k : {}".format(one_minus_ed / num))