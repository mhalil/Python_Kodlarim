"""
SORU:
Yapmak İstediğim; İki Excel dosyasını karşılaştırılarak Ana_Tablodaki verileri güncellemek
Güncel_Kurum_Sayıları tablosunda olup, Ana_Tabloda yoksa olmayan kurumun Ana_tabloya eklenmesi ve Durumu başlığına Yeni Açılış (23.03.2024) olarak not eklenmesi,
Güncel_Kurum_Sayıları tablosunda olmayıp, Ana_tabloda var ise Ana_tablodan bunların silinmesi ve mesaj olarak 'silinen kurumun ilçesi ve okul adının (Örnek;‘Sarıca İlçesi-Sarıca İlkokulu Kapatılmıştır’) şeklinde bildirilmesi
"""

import pandas as pd
df_ana = pd.read_excel("Ana_Tablo.ods")
print("DF_ANA_KURUM:\n", df_ana)

df_guncel = pd.read_excel("Güncel_Kurum_Sayıları.ods")
print("\nDF_GUNCEL_KURUM:\n", df_guncel)


df_ana["Kurum_Kod_Kod1"] = df_ana["KURUM_KODU"].astype(str) + df_ana["KURUM_KODU1"].astype(str)
df_ana = df_ana.set_index("Kurum_Kod_Kod1")
# print("DF_ANA:\n", df_ana)

df_guncel["Kurum_Kod_Kod1"] = df_guncel["KURUM_KODU"].astype(str) + df_guncel["KURUM_KODU1"].astype(str)
df_guncel = df_guncel.set_index("Kurum_Kod_Kod1")
# print("\nDF_GUNCEL:\n", df_guncel)


df_ana_indeks = df_ana.index
# print("DF_ANA:\n", df_ana_indeks)

df_guncel_indeks = df_guncel.index
# print("\nDF_GUNCEL:\n", df_guncel_indeks)


df_guncel["EĞİTİM_KADEMESİ"] = df_ana["EĞİTİM_KADEMESİ"]
# print("DF_ANA:\n", df_ana)
# print("\nDF_GUNCEL:\n", df_guncel)

### Güncelleme Fonksiyonu
def guncelle():
    for indeks in df_ana.index:
        if indeks in df_guncel.index:
            if (df_ana.loc[indeks, "KURUM_ADI"] == df_guncel.loc[indeks, "KURUM_ADI"]):
                continue
            else:
                df_ana.loc[indeks, "KURUM_ADI"] = df_guncel.loc[indeks, "KURUM_ADI"]
                df_ana.loc[indeks, "DURUMU"] = "Okul Adı Değişikliği (27.04.2024)"
guncelle()
# print(df_ana)


eklenecekler = []

for indeks in df_guncel_indeks:
    if indeks not in df_ana_indeks:
        eklenecekler.append(indeks)
# print("\n\nEklenecekler:", eklenecekler)

sil = []

for indeks in df_ana_indeks:
    if indeks not in df_guncel_indeks:
        sil.append(indeks)
# print("Silinecekler:", sil)

def satir_sil(satir):
    df_ana.drop(satir, axis = 0, inplace = True)

for satir in sil:
    satir_sil(satir)
# print("\n\nDF_ANA SİLİNMİŞ HAL:\n", df_ana)


def ekle():
    for veri in eklenecekler:
        df_ana.loc[veri] = df_guncel.loc[veri]
        df_ana.loc[veri, "DURUMU"] = "Yeni Açılış (23.03.2024)"

ekle()
print("\n\nDF_ANA_KURUM NİHAİ HAL:\n", df_ana)
