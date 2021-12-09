sonuc = 1

try:
    girdi = int(input('Faktoriyelini hesaplamak istediginiz sayı değeri giriniz : ')) #Kullanıcıdan bir değer alın ve bunu tamsayıya dönüştür.
    
    if girdi == 0:
        print('0!= 1') # Sıfır faktoriyel 1'e eşittir.
        
    elif girdi < 0:
        print('Faktöriyel, negatif sayılar için tanımsızdır')
            
    else:
        for sayi in range(2, girdi+1): #döngüye başla, 
            sonuc *= sayi #Her bir işlem sonrası Faktoriyel değerini hesaplar 
        print(girdi, '!= ', sonuc, sep="") #Sonucu ekrana yazdırır. 

except:
    print('Geçerli bir değer girin.')

