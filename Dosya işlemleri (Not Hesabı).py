def not_hesapla(satir):

    satir = satir[:-1]

    liste = satir.split(",")

    isim = liste[0]
    vize1 = int(liste[1])
    vize2 = int(liste[2])
    final = int(liste[3])

    harf = ""

    sinav_notu = vize1 * 0.2 + vize2 * 0.3 + final * 0.5

    if (sinav_notu >= 90):
        harf = "AA"

    elif (sinav_notu >= 85):
        harf = "BA"

    elif (sinav_notu >= 80):
        harf ="BB"

    elif (sinav_notu >= 75):
        harf ="CB"

    elif (sinav_notu >= 70):
        harf ="CC"

    elif (sinav_notu >= 65):
        harf ="DC"

    elif (sinav_notu >= 60):
        harf ="DD"

    else:
        harf = "FF"

    return isim + "------------->" + harf + "\n"



with open("Ogrenciler ve notlari.txt", "r", encoding="utf-8") as file:
    not_sonucu = []

    for i in file:
        not_sonucu.append(not_hesapla(i))
    print(not_sonucu)

    with open("sonuclar.txt", "w", encoding="utf-8") as file2:
        for i in not_sonucu:
            file2.write(i)

