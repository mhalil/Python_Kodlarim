"""
Belirtilen 2 sayı aralığında çift olan sayıları "Cift_Sayilark.txt" isimli dosyaya yazdıran basit bir kod.
"""

sayi1 = int(input("Başlangıç sayısını girin: "))
sayi2 = int(input("Bitiş sayısını girin: "))

f = open("Cift_Sayilar.txt", "w")

for sayi in range(sayi1, sayi2+1):
    if sayi % 2 == 0:
        f.write(str(sayi)+"\n")

f.close()