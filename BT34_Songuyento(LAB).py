# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 06:29:59 2024

@author: UNHI
"""

n = int(input("Nhập vào số nguyên dương n: "))
while n < 0:
    n = int(input("Nhập lại số nguyên dương n"))
else:
    songuyento = "có"
    if n <= 2:
        songuyento = "không"
    for i in range(2,n):
        if n % i == 0 :
            songuyento = "không"
            break
    if songuyento == "có":
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải là số nguyên tố")