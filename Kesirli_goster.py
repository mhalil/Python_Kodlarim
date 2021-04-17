'''
Created on Fri Apr 16 21:10:17 2021
@author: Mustafa Halil (@AcikKaynakci)

Belirtilen Ondalıklı sayıyı, Kesirli hale dönüştüren program.

Örnek çıktılar;
0.75 sayısının kesirli gösterimi: 3 / 4
1.25 sayısının kesirli gösterimi: 5 / 4

'''

sayi = float(input("Kesirli halini görmek istediğiniz ondalıklı sayıyı yazın:"))

bol = str(sayi).split('.')      # girilen sayıyı tamsayı ve ondalık kısma böl, liste halinde tut

ts = int(bol[0])                # sayının tamsayı kısmı
ond = int(bol[1])               # sayının ondalık kısmı
ond_uzn = len(str(ond))         # ondalık kısmın basamak sayısı

pay = int(str(ts) + str(ond))   # pay sayı değeri
payda = 10 ** ond_uzn             # payda sayı değeri

def carpan(sayi):               # belirtilen sayı değerini çarpanlara ayırıp liste halinde geri döndüren fonksiyon.
    lst = [1]
    bolen = 2

    for i in range(1,sayi):
        if sayi % bolen == 0:
            sayi /= bolen
            lst.append(bolen)
        else:
            bolen += 1
    return lst
 

def carp(liste):                # belirtilen liste içerisindeki tüm değerleri çarpıp sunuç döndüren fonksiyon. (liste içerisi sadece sayıdan oluşmalı)
    sonuc = 1
    if liste == []:
        sonuc = 1
    else:
        for i in liste:
            sonuc *= i
    return sonuc


pay_carpan = carpan(pay)           # pay sayı değerini çarpanlarına ayır, listele
payda_carpan = carpan(payda)           # payda sayı değerini çarpanlarına ayır, listele


def sil(a, l1, l2):             # 2 liste (l1 ve l2) içerisindeki ortak sayı değerini (a) silen fonksiyon.
    if ((a in l1) and (a in l2)):
        l1.remove(a)
        l2.remove(a)

index = 0

while index <= len(pay_carpan):    # index değeri, pay değerinin çarpanları sayısından küçük eşit olduğu sürece döngüyü çalıştır.
    try:
        a = pay_carpan[index]       # pay'ın tek çarpanlar değeri
           
        if a in payda_carpan:                   # eğer pay'ın çarpan değeri payda çarpan listesinde varsa ...
            sil(a, pay_carpan, payda_carpan)    # ortak çarpan değerini sil
        else:                                   # değilse
            index +=1                           # pay çarpan listesindeki sonraki sayıya geçmek için index değerini 1 artır.
         
    except IndexError:              # IndexError hatası alırsak ...
        break                       # döngüyü sonlandır / bitir.

print(sayi, "sayısının kesirli gösterimi:", carp(pay_carpan),"/", carp(payda_carpan)) # pay çarpanlarındaki değerlerle, payda çarpanlarındaki  değerleri (her iki listedeki ortak değerler silindikten sonra) kendi içerisinde çarp ve sonuç olarak ekrana yazdır.
