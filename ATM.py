bakiye = 2500

while True:
    
    print("""
    **********************
    ATM'ye hoş geldiniz.
    **********************
    
    Lütfen İşleminizi Seçin ;
    1 - Bakiye Sorgulama
    2 - Para Yatırma
    3 - Para Çekme
    Q - Çıkmak için
    """)

    
    islem = input("İşlem No.: ")
    
    if islem == "1":
        print("Mevcut Bakiyeniz: {} TL'dir.".format(bakiye))
    
    
    elif islem == "2":
        yatirilan = float(input("Yatırmak istediğiniz Miktarı Girin: "))
        bakiye += yatirilan
        print("Toplam Bakiye: {} TL'dir.".format(bakiye))
    
    elif islem == "3":
        cekilen = float(input("Çekmek istediğiniz miktarı girin: "))
        if cekilen > bakiye:
            print("Çekmek istediğiniz tutar, Bakiye Tutarınızın üzerindedir.")
        else:
            bakiye -= cekilen
            print("Mevcut bakiyeniz: ", bakiye, "'TL dir.")
    
    elif islem == "Q" or islem == "q":
        print("İşlem Sonlandı. Kartınızı almayı unutmayın.")
        break
    
    else:
        print("Hatalı seçim yaptınız, Geçerli bir seçenek seçin lütfen !")
    
