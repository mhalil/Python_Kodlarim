import pandas as pd
import re

df = pd.read_excel("pandas_re_veri.ods")
print("\n\ndf Veri çerçevesi\n:", df)

# MALZEME sütunundaki veriler içerisinde 2 ile 5 haneli rakam bulunan değerleri gösterir.
# print(df.loc[df["MALZEME"].str.contains(r"\d{2,5}", regex=True)])

# MALZEME sütunundaki veriler içerisinde 3 ile 5 haneli rakam bulunan değerleri yeni veri çerçevesine ata.
df2 = df.loc[df["MALZEME"].str.contains(r"\d{3,5}", regex=True)]
print("\n\ndf2 Veri çerçevesi\n:", df2)

def sayi(x):
    desen = r"\d+"
    deger = re.findall(desen, x)
    return deger

# MALZEME sütunundaki veriler içerisindeki sayıları, "DEGERLER" isimli sütunda liste halinde ekle
df2["DEGERLER"] = df2["MALZEME"].apply(sayi)
print("\n\ndf2 Veri çerçevesi - APPLY() uygulanmış hali\n:", df2)

# Dosyayı "DEGER.ODS" ismi ile kaydet
df2.to_excel("deger.ods")