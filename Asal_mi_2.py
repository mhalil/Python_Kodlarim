
sayi = int(input("Lütfen bir tamsayı girin: ")) #Kullanıcıdan bir tamsayı girmesini istiyoruz
aralik = range(2,sayi+1) #2'den başlamak üzere, girilen tamsayıyı içine alacak bir aralık belirliyoruz
listem = list() #Boş bir liste oluşturuyoruz.

for bolen in aralik:
    if sayi % bolen == 0: # Girilen sayıyı,  2'den başlayarak, (girilen sayı da dahil olacak şekilde) aralık içindeki tüm sayılara bölüyoruz.
        listem.append(bolen) # eğer kalan 0 ise (yani tam bölünüyorsa) listeye ekliyoruz.

if listem[0] == sayi: # Bu ifadeyi şu şekilde de yazarsak aynı sonucu elde edebiliriz.--> if len(listem) == 1
    print(sayi, " asal bir sayıdır.") #liste içeriğindeki sayı, kullanıcının girdiği sayı ise ya da if len(listem) == 1 bu ifade kullanılmış ise, listede 1 adet eleman varsa, ekrana, bu sayının asal bir sayı olduğunu yazdırıyoruz.
else:
    print("sayı asal değildir") #aksi halde ekrana, bu sayının asal bir sayı olmadığını yazdırıyoruz.