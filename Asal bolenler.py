# 1099511627776 sayisinin sadece 1 tane asal boleni var.

tam_bolenler = list()
asal_bolenler = list()

def bolenler(sayi):
	for elm in range(2,sayi+1):
		if (sayi % elm == 0):
#			print(elm)
			tam_bolenler.append(elm)

def asal_mi(x):
	for i in range(2,x):
		if (x % i == 0):
			return False
	return True

girdi = int(input("Tam bölenlerini bulmak istediğiniz sayıyı yazın: "))

bolenler(girdi)
print(girdi, " sayısının tam bölenleri şunlardır:\n", tam_bolenler, sep="")

for i in tam_bolenler:
	if (asal_mi(i)):
		asal_bolenler.append(i)

print('asal bolenler:', asal_bolenler)
