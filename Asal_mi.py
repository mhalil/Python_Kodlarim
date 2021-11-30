def asal(x):
    for i in range(2,((x//2)+1)):
        if (x % i == 0):
            return False

    return True


while True:
    x = input("sayi degeri girin: ")

    if (x == "q"):
        break

    else:
        x = int(x)

        if (asal(x)):
            print(x, "asaldir")
        else:
            print(x, "asal degil.")




