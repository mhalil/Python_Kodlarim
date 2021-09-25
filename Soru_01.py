#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 00:04:38 2021

@author: Mustafa Halil (@AcikKaynakci)
"""

# a, b ve c sıfırdan ve birbirinden farklı 3 rakamdır.
# abc, cba, cab sayılarından her biri 13, 17, 5'e  ve tümü 9'a tam bölünüyor. Buna göre a*b*c kactir?

rakamlar = range (1,10)
for a in rakamlar:
    for b in rakamlar:
        for c in rakamlar:
            if (a != b, a != c, b != c):
                s13 = str(a) + str(b) + str(c)
                s17 = str(c) + str(b) + str(a)
                s5 = str(c) + str(a) + str(b)
                if (int(s13) % 13 == 0) and (int(s17) % 17 == 0) and (int(s5) % 5 == 0):
                    print(f"a: {a}, b: {b}, c: {c}")
                    print("a * b * c =", a * b * c)
            
