"""
SORU:
Merhaba Arkadaşlar;

Yapmak İstediğim; İki Excel dosyasını karşılaştırılarak Ana_Tablodaki verileri güncellemek
Güncel_Kurum_Sayıları tablosunda olup, Ana_Tabloda yoksa olmayan kurumun Ana_tabloya eklenmesi ve Durumu başlığına Yeni Açılış (23.03.2024) olarak not eklenmesi,
Güncel_Kurum_Sayıları tablosunda olmayıp, Ana_tabloda var ise Ana_tablodan bunların silinmesi ve mesaj olarak 'silinen kurumun ilçesi ve okul adının (Örnek;‘Sarıca İlçesi-Sarıca İlkokulu Kapatılmıştır’) şeklinde bildirilmesi

"""

import pandas as pd
df_ana = pd.read_excel("Ana_Tablo.ods")
# print(df_ana.head())

df_guncel = pd.read_excel("Güncel_Kurum_Sayıları.ods")
# print(df_guncel.head())

df_ana["Kurum_Kod_Ad"] = df_ana["KURUM_KODU"].astype(str) + df_ana["KURUM_ADI"]
df_ana = df_ana.set_index("Kurum_Kod_Ad")
# print(df_ana.head())

df_guncel["Kurum_Kod_Ad"] = df_guncel["KURUM_KODU"].astype(str) + df_guncel["KURUM_ADI"]
df_guncel = df_guncel.set_index("Kurum_Kod_Ad")
# print(df_guncel.head())

df_ana_indeks = df_ana.index
# print(df_ana_indeks)

df_guncel_indeks = df_guncel.index
# print(df_guncel_indeks)


# ekle = []

# for indeks in df_guncel_indeks:
#     if indeks not in df_ana_indeks:
#         ekle.append(indeks)

# print("Eklenecekler:", ekle)

# sil = []

# for indeks in df_ana_indeks:
#     if indeks not in df_guncel_indeks:
#         sil.append(indeks)

# print("Silinecekler:", sil)


