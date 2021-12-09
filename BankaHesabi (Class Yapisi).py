class BankaHesabi():
    def __init__(self, musteri):
        self.musteri = musteri
        self.bakiye= 0.0
    
    def getBakiye_ogren(self):
        print("Güncel Bakiyeniz:", self.bakiye)
    
    def para_yatir(self, miktar):
        self.bakiye += miktar
        print(f"Hesabiniza {miktar} TL yatirildi")
        return self.bakiye
    
    def para_cek(self, miktar):
        self.bakiye -= miktar
        print(f"Hesabinizdan {miktar} çekildi")
        return self.bakiye

hesapNo001 = BankaHesabi("Mustafa Halil")

print(hesapNo001.musteri)
print(hesapNo001.bakiye)

hesapNo001.para_yatir(1000)
hesapNo001.getBakiye_ogren()
hesapNo001.para_cek(500)
hesapNo001.getBakiye_ogren()

hesapNo001.para_yatir(2000)
hesapNo001.getBakiye_ogren()
hesapNo001.para_cek(1000)
hesapNo001.getBakiye_ogren()

