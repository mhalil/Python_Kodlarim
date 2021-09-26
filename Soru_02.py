# SORU 1: Rakamları toplamının 7 katına eşit olan iki basamaklı kaç tane doğa sayı vardır?

for sayi in range (10,100):
	if (sayi == (int(str(sayi)[0])+ int(str(sayi)[1]))*7):
		print (sayi)

#ÇIKTI:
# 21
# 42
# 63
# 84
