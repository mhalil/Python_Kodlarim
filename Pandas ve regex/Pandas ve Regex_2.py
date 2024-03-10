import pandas as pd
import re

dosya = pd.read_excel("BİNA_KULLANIM.xlsx")
df = pd.DataFrame(dosya,columns=["KURUM_KODU", "TİPİ","İLÇE","KULLANIM_ALANI","OKUL_KURUM_ADI","SAYISI"])  
print("\nBİNA_KULLANIM\n\n", df)

desen_bilgi = r"\w*BİLGİ\w*"
desen_orta = r"\w*orta\w*"

def like_bilgi(x):
    sonuc  =  re.search(desen_bilgi, x, re.IGNORECASE)
    if sonuc:
        return x

def like_orta(x):
    sonuc  =  re.search(desen_orta, x, re.IGNORECASE)
    if sonuc:
        return x    

df["KULLANIM_ALANI"] = df["KULLANIM_ALANI"].apply(like_bilgi)
df.dropna(axis = 0, inplace = True)
print("\n\nBİLGİ SONUÇLARI:\n\n", df)

df["OKUL_KURUM_ADI"] = df["OKUL_KURUM_ADI"].apply(like_orta)
df.dropna(axis = 0, inplace = True)
print("\n\nORTA SOUÇLARI:\n\n", df)
