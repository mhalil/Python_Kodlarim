# Soru_03: Karekökü rakamları toplamına eşit olan sayı kaçtır?

#Tek haneli sayılarda, karekökü kendisine eşit olan, 2 ve yukarı haneye sahip sayılarda, karekökü rakamları toplamina esit ilan sayılar (1 ile 10.000 arası);

import math

for sayi in range(1,10000):
	a = str(sayi)
	if (len(a) == 1):
		if (math.sqrt(sayi) == (int(a[0]))): # karekoku kendisine esit olan sayi icin "== sayi" da yazilabilir.
			print (sayi)

	elif (len(a) == 2):
		if (math.sqrt(sayi) == (int(a[0]) + int(a[1]))):
			print(sayi)

	elif (len(a) == 3):
		if (math.sqrt(sayi) == (int(a[0]) + int(a[1]) + int(a[2]))):
			print (sayi)

	elif (len(a) == 4):
		if (math.sqrt(sayi) == (int(a[0]) + int(a[1])) + int(a[2]) + int(a[3])):
			print (sayi)

#ÇIKTI:
# 1
# 81
# ------------------------------
##### ALTERNATİF (SÜPER) ÇÖZÜM; #####

def fonk(a, b):
    for num in range(a, b):
        if num ** 0.5 == sum(map(int, str(num))):
            yield num

uretec = fonk(1,10000)

for i in uretec:
    print(i)
