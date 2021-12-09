def ekok(x,y):
    listex = []
    listey = []

    for i in range (1,x*y):
        listex.append(i * x)
        listey.append(i * y)

        for a in listex:
            if a in listey:
                return(a)
    return a

print("En Küçük Ortak Bölenlerini bulmak istediğiniz sayıları belirtin. (Or. 16 ve 24)")
print("#" * 80)

girdi1 = int(input("1. sayısı girin: "))
girdi2 = int(input("2. sayısı girin: "))

print(ekok(girdi1, girdi2))
