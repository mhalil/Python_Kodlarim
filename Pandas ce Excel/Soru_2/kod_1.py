"""
Bir Excel dosyasından diğer Excel dosyasına veri almak istiyorum.

Yapmak istediğim;
1- Ana Tablo’daki KURUM_KODU, Öğrenci_Sayıları tablosundaki "KURUM_KODU"na eşitse,
2- Ana_Tablo’daki EĞİTİM_KADEMESİ, Öğrenci_Sayıları tablosundaki "EĞİTİM_KADEMESİ"ne eşitse (OKULÖNCESİ hariç)
3- Öğrenci_Sayıları tablosundaki, öğrenci sayıları sütunlarını (ERKEK_ÖĞRENCİ, KIZ_ÖĞRENCİ ,TOPLAM_ÖĞRENCİ) Ana Tablo’daki aynı addaki sütunlara toplamlarını getirmesi
 """

###

import pandas as pd
from openpyxl import Workbook

dosya = pd.read_excel("ANA_TABLO.ods") 
df_ana= pd.DataFrame(dosya)
# print("\n\n'df_ana: '\n", df_ana)

dosya = pd.read_excel("ÖĞRENCİ_SAYILARI.ods")
df_ogrenci = pd.DataFrame(dosya)  
# print("\n\n'df_ogrenci: '\n", df_ogrenci)

df_ana["Kurum_Egitim"] = df_ana["KURUM_KODU"].astype(str) + "_" + df_ana["EĞİTİM_KADEMESİ"]   # df_ana["KURUM_KODU"].apply(str) şeklinde de kullanılabilir.
df_ana = df_ana.set_index("Kurum_Egitim")
# print("\n\n'df_ana - Kurum_Egitim: '\n", df_ana)

df_ogrenci["Kurum_Egitim"] = df_ogrenci["KURUM_KODU"].apply(str) + "_" + df_ogrenci["EĞİTİM_KADEMESİ"]
df_ogrenci = df_ogrenci.set_index("Kurum_Egitim")
# print("\n\n'df_ogrenci indeks Kurum_Egitim: '\n", df_ana)

df_ana["ERKEK_ÖĞRENCİ"] = df_ogrenci.groupby("Kurum_Egitim").sum()["ERKEK_ÖĞRENCİ"]
# print("\n\n'df_ana - erkek: '\n", df_ana)

df_ana["KIZ_ÖĞRENCİ"] = df_ogrenci.groupby("Kurum_Egitim").sum()["KIZ_ÖĞRENCİ"]
# print("\n\n'df_ana - kız: '\n", df_ana)

df_ana["TOPLAM_ÖĞRENCİ"] = df_ana["ERKEK_ÖĞRENCİ"] + df_ana["KIZ_ÖĞRENCİ"]
# print("\n\n'df_ana - toplam = (Erkek + Kız): '\n", df_ana)

df_ana = df_ana.set_index("KURUM_KODU")
# print("\n\n'df_ana - indeks KURUM_KODU: '\n", df_ana)

########################################################################################
# df_ana.to_excel("ANA_TABLO.ods")  # dosya içeriğindeki tüm sekmeleri siliyor.
########################################################################################

"""
Pandas’ın ExcelWriter metodundaki mode parametresi işimizi çözüyor.
mode parametresi iki değer alabiliyor. {w : yaz, a : ekle}, Varsayılan mod w yani yazma modu.

Önce df_ana verisini istediğimiz gibi elde ediyoruz. Yazma aşamasına getiriyoruz.
Ardından Excel dosyasındaki İlgili sekmeyi silip, aynı isimle yeniden EKLİYORUZ
Kaynaklar

    python - Overwrite an excel sheet with pandas dataframe without affecting other sheets - Stack Overflow
    pandas.ExcelWriter — pandas 2.2.1 documentation

"""

filename = "ANA_TABLO.xlsx"

def write_excel(filename,Sayfa1,dataframe):
    with pd.ExcelWriter(filename, engine='openpyxl', mode='a') as writer: 
        workBook = writer.book
        try:
            workBook.remove(workBook[Sayfa1])
        except:
            print("Worksheet does not exist")
        finally:
            dataframe.to_excel(writer, sheet_name=Sayfa1,index=False)
            writer._save()

write_excel(filename,'Sayfa1',df_ana)


