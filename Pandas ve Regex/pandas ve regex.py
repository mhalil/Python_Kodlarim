# Pandas ve Regex kullanılarak ... İÇEREN veriyi "STRING Metodu" kullanarak bulmaya ait kod

import pandas as pd
import re

df = pd.read_excel("pandas_re_veri.ods")
# print(df)

# MALZEME sütunundaki veriler içerisinde 2 ile 5 rakam bulunan değerleri gösterir.
print(df.loc[df["MALZEME"].str.contains("\d{2,5}", regex=True)])


def sayi(x):
    desen = r"\d+"
    deger = re.findall(desen, x)
    return deger

# MALZEME sütunundaki veriler içerisindeki sayıları, "DEGERLER" isimli sütunda liste halinde ekle
df["DEGERLER"] = df["MALZEME"].apply(sayi)
print(df)

# Dosyayı "DEGER.ODS" ismi ile kaydet
df.to_excel("deger.ods")
