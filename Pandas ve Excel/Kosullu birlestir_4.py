import pandas as pd

dosya = pd.read_excel("ANA_TABLO.xlsx") 
df_ana= pd.DataFrame(dosya,columns=["KURUM_KODU", "TİPİ","İLÇE","OKUL_KURUM_ADI","DERSLİK_SAYISI"])
# print("\n\nANA_TABLO\n", df_ana)

dosya = pd.read_excel("BİNA_KULLANIM_Tekrarsiz.xlsx")
df_bina = pd.DataFrame(dosya,columns=["KURUM_KODU", "TİPİ","İLÇE","KULLANIM_ALANI","OKUL_KURUM_ADI","SAYISI"])  
# print("\n\nBİNA_KULLANIM\n", df_bina)

df1 = df_bina[df_bina["KULLANIM_ALANI"].str.contains("TOPLAM DERSLİK")]
# print("\n\n 'TOPLAM DERSLİK' FİLTRELİ df_bina TABLOSU:\n", df1)

df_ana = df_ana.set_index("KURUM_KODU") # indeks değerleri ayarlanıyor.
df1 = df1.set_index("KURUM_KODU")       # indeks değerleri ayarlanıyor.
# print("İndeksli ANA_TABLO:\n", df_ana)
# print("İndeksli df1 Tablosu:\n", df1)

df_ana["DERSLİK_SAYISI"] = df1["SAYISI"]
# print("\n\nNİHAİ ANA_TABLO:\n", df_ana)

df_ana.to_excel("ANA_TABLO_SONUC_4.xlsx")