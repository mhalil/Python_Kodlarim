"""
Soru:
TOLGA Kelimesinin harflerinin yerleri değiştirilerek oluşturulan kelimeler alfabetik olarak sıralanırsa 81. kelime ne olur?
"""

from itertools import permutations

kelime = "TOLGA"
listem = []

uret = list(permutations(kelime,len(kelime)))

for i in uret:
    if "".join(i) not in listem:
        listem.append("".join(i))

listem.sort() #Liste içeriğini alfabetik olarak sıralar.
print(listem[80]) # Sıralama 0'dan başladığı için listenin 80 numaralı endeksi aslında 81. değerdir.

# aşağıdaki kodlar, Tüm lise içeriğini liste sırasıyla birikte ekrana yazdırır.
# for i,j in enumerate(listem,1):
#     print(f"{i}. Kelime: {j}")

