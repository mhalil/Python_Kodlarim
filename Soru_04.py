# Soru_04: 3, 6, 10, 13, 17, ... sayı dizisinin 35. terimi kaçtır?

a = [3]
b = [3,4]

for i in range(20):
	a.append (a[-1] + b[0])
	a.append (a[-1] + b[1])
	if len(a) == 35:
		print("listedeki eleman sayisi:", len(a))
		print (a)

# ÇIKTI:
# [3, 6, 10, 13, 17, 20, 24, 27, 31, 34, 38, 41, 45, 48, 52, 55, 59, 62, 66, 69, 73, 76, 80, 83, 87, 90, 94, 97, 101, 104, 108, 111, 115, 118, 122]

# "Beatty Sequence" inceleyin.
# AşağıYuvarla(i*(2+√2))
#
# (Cevap: 119)

import math
for i in range(1, 36):
     print(i, math.floor(i*(2+math.sqrt(2))))

# ÇIKTI:

# 1 3
# 2 6
# 3 10
# ...
# ...
# 33 112
# 34 116
# 35 119

import math
listem = []

for i in range(1, 36):
     listem.append(math.floor(i*(2+math.sqrt(2))))

print (listem)

# ÇIKTI:
# [3, 6, 10, 13, 17, 20, 23, 27, 30, 34, 37, 40, 44, 47, 51, 54, 58, 61, 64, 68, 71, 75, 78, 81, 85, 88, 92, 95, 99, 102, 105, 109, 112, 116, 119]
