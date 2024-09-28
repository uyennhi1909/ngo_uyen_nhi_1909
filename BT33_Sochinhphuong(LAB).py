# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 06:23:25 2024

@author: UNHI
"""
n = int(input("Nhập vào số n: "))
while n < 0:
    n = int(input("Vui lòng nhập lại số nguyên dương n: "))
else:
    if n ** 1/2 == int(n ** 1/2):
        print(f"{n} là số chính phương")
    else:
        print(f"{n} không phải là số chính phương")
