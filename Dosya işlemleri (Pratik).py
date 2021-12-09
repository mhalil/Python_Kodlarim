def kopyala(orj):
    with open (orj, "r", encoding="UTF-8") as dosya:
        with open (orj+"_kopyası.txt", "w", encoding="UTF-8") as kopya_:
            for i in dosya.readlines():
                kopya_.writelines(i)

girdi1 = input("Kopyalamak istediginiz dosya adını ve uzantisini belirtin (Or: halil.txt ) :")
kopyala(girdi1)


def terscevir(orj):
    with open (orj, "r", encoding="UTF-8") as dosya:
        with open (orj+"_tersi.txt", "w", encoding="UTF-8") as ters_:
            for i in dosya.readlines():
                ters_.writelines(i[::-1])

girdi2 = input("İçeriğini ters çevirmek istediginiz dosya adını ve uzantisini belirtin (Or: halil.txt ) :")
                
terscevir(girdi2)


