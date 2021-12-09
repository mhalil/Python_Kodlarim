liste = list()

sayi_miktari = int(input("Kaç adet sayı girişi yapmak istiyorsunuz?: "))

for i in range(sayi_miktari):
    giris = int(input("{}. Sayı girin: ". format(i+1)))
    liste.append(giris)

# print(liste) #ekleme sırasına göre liste içeriğini görmek isterseniz bu kodu kullanın
liste.sort()
# print(liste) #küçükten büyüğe sıralanmış liste içeriğini görmek isterseniz bu kodu kullanın

print("Girmiş olduğunuz en küçük sayı:", liste[0])
print("Girmiş olduğunuz en büyük sayı:", liste[-1])
