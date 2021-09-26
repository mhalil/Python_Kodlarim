# Soru_07: 23 Ağustos 12:25’e 10.000 dakika eklersek tarih ve saat ne olur?

import datetime
# import locale

bugun = datetime.datetime(2019, 8, 23, 12, 25)
ilave = datetime.timedelta(seconds=600000)
sonuc = bugun + ilave

print(datetime.datetime.ctime(sonuc))

# print(locale.setlocale(locale.LC_ALL,'Turkish.Turkey_1254'))

# ÇIKTI:
# Fri Aug 30 11:05:00 2019
