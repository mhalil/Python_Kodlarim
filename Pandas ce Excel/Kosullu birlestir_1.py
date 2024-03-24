"""
İSTENİLEN:
Koşul 1: Eğer ANA_TABLO'daki "KURUM_KODU", BİNA_KULLANIM tablosundaki "KURUM_KODU"na eşitse ve 
Koşul 2: BİNA_KULLANIM tablosundaki "KULLANIM_ALANI" sütunu "8- TOPLAM DERSLİK SAYISI" na eşitse,

BİNA_KULLANIM tablosundaki "SAYISI" sütununu ANA_TABLO'daki "DERSLİK_SAYISI" sütununa yazdır. Yoksa "0" yazdır.
"""

import pandas as pd

dosya = pd.read_excel("ANA_TABLO.xlsx", index_col=0) 
df_ana= pd.DataFrame(dosya,columns=["TİPİ","İLÇE","OKUL_KURUM_ADI","DERSLİK_SAYISI"])
print("ANA_TABLO\n", df_ana)

dosya = pd.read_excel("BİNA_KULLANIM.xlsx", index_col=0)
df_bina = pd.DataFrame(dosya,columns=["TİPİ","İLÇE","KULLANIM_ALANI","OKUL_KURUM_ADI","SAYISI"])  
print("BİNA_KULLANIM\n", df_bina)


kosul = df_bina["KULLANIM_ALANI"] == "8- TOPLAM DERSLİK SAYISI"
df_gecici = df_bina[kosul]    # "df_bina" isimli Veri Çerçevesinde "KULLANIM_ALANI" sütunu "8- TOPLAM DERSLİK SAYISI" ifadesine eşit olan verilerden müteşekkil geçicici bir Veri Çerçevesinde oluşturuyoruz.

df_pivot = pd.pivot_table(
    data = df_gecici, 
    index="KURUM_KODU", 
    values="SAYISI", 
    aggfunc="sum")    # "df_gecici" isimli Veri Çerçevesinde aynı KURUM_KODU'na sahip birden fazla veri olduğu için bu değerleri toplayarak, her Kurum Koduna ait bir değer içeren geçici bir Veri Çerçevesinde daha oluşturuyoruz.

df_pivot.columns = ["DERSLİK_SAYISI"]    # "SAYISI" olan sütun adını "DERSLİK_SAYISI" olarak değiştiriyoruz.

df_ana.drop("DERSLİK_SAYISI",axis=1, inplace=True)   # "df_ana" isimli  Veri Çerçevesinde  "DERSLİK_SAYISI" sütununda veri olmadığı için siliyorum.

df_sonuc =pd.merge(df_ana, df_pivot, on = "KURUM_KODU", how = "left")    # "df_ana" ve "df_pivot" Veri Çerçevelerini, df_ana'yı baz alarak birleştiriyorum.

df_sonuc.to_excel("ANA_TABLO_SONUC1.xlsx")



"""
Kodu denerken kullandığım veriler;

```python
ANA_TABLO
              TİPİ      İLÇE                OKUL_KURUM_ADI  DERSLİK_SAYISI
KURUM_KODU                                                               
11          RESMİ    SARICA          HalkEğitimi Merkezi              NaN
12          RESMİ    BÜNYAN             Atatürk İlkokulu              NaN
13          RESMİ  ŞARKIŞLA            Atatürk Ortaokulu              NaN
14          RESMİ    SARICA             Kırboğa İlkokulu              NaN
15          RESMİ    SARICA            Kırboğa Ortaokulu              NaN
16          RESMİ    BÜNYAN           Halk Eğitim Merkezi             NaN
17          RESMİ  ŞARKIŞLA           Kutu Tepe İlkokulu              NaN
18          RESMİ    SARICA           Kutu Tepe Ortaokulu             NaN
19          RESMİ    SARICA             Ortaköy İlkokulu              NaN
20          RESMİ    BÜNYAN            Ortaköy Ortaokulu              NaN
21          RESMİ  ŞARKIŞLA          İmam Hatip Ortaokulu             NaN
22          RESMİ    SARICA  Çok Programlı Anadolu Lisesi             NaN
23          RESMİ    SARICA              Sanica Anaokulu              NaN
24          RESMİ    BÜNYAN              Dereli İlkokulu              NaN
25          RESMİ  ŞARKIŞLA             Dereli Ortaokulu              NaN
26          RESMİ    SARICA              Atatürk İlkokulu             NaN

BİNA__KULLANIM
              TİPİ       İLÇE            KULLANIM_ALANI         OKUL_KURUM_ADI  SAYISI
KURUM_KODU                                                                           
11          RESMİ     SARICA  8- TOPLAM DERSLİK SAYISI   Halk Eğitimi Merkezi      22
11          RESMİ     SARICA       BİLGİSAYAR SAYISI     Halk Eğitimi Merkezi      25
12          RESMİ     BÜNYAN  8- TOPLAM DERSLİK SAYISI       Atatürk İlkokulu      12
13          RESMİ   ŞARKIŞLA  8- TOPLAM DERSLİK SAYISI     Atatürk Ortaokulu        5
14          RESMİ     SARICA  8- TOPLAM DERSLİK SAYISI      Kirboga İlkokulu        4
12          RESMİ     BÜNYAN       BİLGİSAYAR SAYISI         Atatürk İlkokulu       9
14          RESMİ     SARICA  8- TOPLAM DERSLİK SAYISI      Kirboga İlkokulu       12
15          RESMİ     SARICA       BİLGİSAYAR SAYISI       Kirboga Ortaokulu       21
16          RESMI     BUNYAN  8- TOPLAM DERSLİK SAYISI    Halk Eğitim Merkezi      14
17          RESMİ  ŞARKIŞLA   8- TOPLAM DERSLİK SAYISI     Kutu Tepe İlkokulu      12
17          RESMİ   ŞARKIŞLA       BİLGİSAYAR SAYISI      Kutu Tepe İlkokulu        5
18          RESMİ     SARICA       BİLGİSAYAR SAYISI      Kutu Tepe Ortaokulu       8
19          RESMİ     SARICA       BİLGİSAYAR SAYISI         Ortaköy İlkokulu       5
16          RESMI     BUNYAN  8- TOPLAM DERSLİK SAYISI    Halk Eğitim Merkezi       9
20          RESMİ     BÜNYAN  8- TOPLAM DERSLİK SAYISI  Ortaköy Ortaokulu İS-      10
21          RESMİ   ŞARKIŞLA       BİLGİSAYAR SAYISI    İmam Hatip Ortaokulu        4
22          RESMİ     SARICA  8- TOPLAM DERSLİK SAYISI  Çok Programlı Anadolu       5
23           ÖZEL     SARICA  8- TOPLAM DERSLİK SAYISI   OZELSARICA ANAOKULU       12
23          RESMİ     SARICA       BİLGİSAYAR SAYISI     ÖZELSARICA ANAOKULU        7
24          RESMİ     BÜNYAN  8- TOPLAM DERSLİK SAYISI        Dereli İlkokulu       4
25          RESMİ   ŞARKIŞLA  8- TOPLAM DERSLİK SAYISI      Dereli Ortaokulu        5
26          RESMİ     SARICA       BİLGİSAYAR SAYISI         Atatürk İlkokulu       4
26          RESMİ     SARICA  8- TOPLAM DERSLİK SAYISI      Atatürk İlkokulu        7
```

ÇIKTI:
```python
KURUM KODU   TİPİ      İLÇE               OKUL_KURUM_ADI   DERSLİK_SAYISI
11          RESMİ    SARICA          HalkEğitimi Merkezi             22.0
12          RESMİ    BÜNYAN             Atatürk İlkokulu             12.0
13          RESMİ  ŞARKIŞLA            Atatürk Ortaokulu              5.0
14          RESMİ    SARICA             Kırboğa İlkokulu             16.0
15          RESMİ    SARICA            Kırboğa Ortaokulu              NaN
16          RESMİ    BÜNYAN           Halk Eğitim Merkezi            23.0
17          RESMİ  ŞARKIŞLA           Kutu Tepe İlkokulu            12.0
18          RESMİ    SARICA           Kutu Tepe Ortaokulu             NaN
19          RESMİ    SARICA             Ortaköy İlkokulu              NaN
20          RESMİ    BÜNYAN            Ortaköy Ortaokulu             10.0
21          RESMİ  ŞARKIŞLA          İmam Hatip Ortaokulu             NaN
22          RESMİ    SARICA  Çok Programlı Anadolu Lisesi             5.0
23          RESMİ    SARICA              Sanica Anaokulu             12.0
24          RESMİ    BÜNYAN              Dereli İlkokulu              4.0
25          RESMİ  ŞARKIŞLA             Dereli Ortaokulu              5.0
26          RESMİ    SARICA              Atatürk İlkokulu             7.0
```
"""
