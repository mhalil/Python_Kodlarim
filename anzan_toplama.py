# Anzan tekniği ile toplama pratiği yapmak için hazırlanan kod.

import time, random

toplam = 0

# islem_sayisi = int(input("işlem sayısını belirtin: "))
islem_sayisi = 2    # işlem sayısını

# sure = int(input("bekleme süresi belirtin: "))
sure = 2    # bekleme süresi (sn.)

for _ in range(islem_sayisi):
    sayi = random.randint(10,20)
    toplam += sayi
    print(sayi)
    time.sleep(sure)

sonuc = int(input("sonucunuzu girin: "))

if sonuc == toplam:
    print("tebrikler")
else:    
    print("Maalesef, sayıların toplamı:", toplam)