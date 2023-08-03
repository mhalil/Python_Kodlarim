"""
String ifade içinde rakamla başlayan heceleri, sona taşıyan fonksiyon. 
Örneğin '65 Van'ın Plakası' string ifadesi 'Van'ın Plakası 65' olarak değiştirilir.
"""

import pandas as pd

df = pd.DataFrame({"kategori" : ["telefon", "bilgisayar", "telefon", "telefon", "bilgisayar", "telefon", "telefon", "bilgisayar", "bilgisayar","bilgisayar"],
                    "model" : ["14_pro_max iphone" , "15S-FQ2028NTI 2N2M9EA Hewlett Packard", "12-Pro Xiaomi Redmi Note", "Samsung Galaxy S22", "13VI-069TR MSI TITAN GT77HX", "13 iphone", "12T-Pro Xiaomi", "Apple Macbook Air MGN93TU-A M1", "5530 Dell Gaming G15 G155530013WH", "Asus TUF Gaming F15 FX506HE-HN011"]
                    })

# print(df.head(10))

def duzelt(cumle:str):    # String ifade içindeki rakamla başlayan kelimeleri, cümlenin sonuna taşıyan fonksiyon.
    gecici_metin = []    # String ifade içinde bulunan metinlerin depolanacağı gecici liste.
    gecici_rakam = []    # String ifade içinde bulunan rakamların depolanacağı gecici liste.
    rakam = "0123456789"    # hecelerin rakamla başlayıp başlamadığının kontrolü için kullanılan değişken. 

    kelimeler = cumle.split(" ") # String ifadeyi " " boşluk karakterine göre ayırıyoruz.

    for kelime in kelimeler:
        if kelime[0] in rakam:
            gecici_rakam.append(kelime)
        else:
             gecici_metin.append(kelime)
    
    yeni_cumle_listesi = gecici_metin + gecici_rakam    # "gecici_metin" ve "gecici_rakam" listeleribi birleştiriyoruz.
    yeni_cumle = " ".join(yeni_cumle_listesi).upper()   # "yeni_cumle_listesi" listesinde bulunan öğeleri birleştirip tüm harfleri büyük harfe çeviriyoruz

    return yeni_cumle.strip()    # strip() metodu ile String ifadenin başında ve sonunda bulunan boşlukları temizliyoruz.

df["model_duzenli"] = df["model"].apply(duzelt)
print(df.head(10))