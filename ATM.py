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
    bakiye = 2500
    
    islem = input("İşlem No.: ")
    
    if islem == "1":
        print("Mevcut Bakiyeniz: {} TL'dir.".format(bakiye))
    
    
    elif islem == "2":
        yatirilan = float(input("Yatırmak istediğiniz Miktarı Girin: "))
        print("Toplam Bakiye: {} TL'dir.".format(bakiye + yatirilan))
    
    elif islem == "3":
        cekilen = float(input("Çekmek istediğiniz miktarı girin: "))
        print("Mevcut bakiyeniz: ", bakiye - cekilen, "'TL dir.")
    
    elif islem == "Q" or islem == "q":
        print("İşlem Sonlandı. Kartınızı almayı unutmayın.")
        break
    
