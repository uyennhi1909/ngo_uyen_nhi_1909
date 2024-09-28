# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:59:35 2024

@author: UNHI
"""

n = int(input("Nhập số N: "))
while n <= 0:
    n = int(input("Nhập số N: "))
if n <= 2:
    print(f"{n} không phải là số nguyên tố")
for i in range(2,n):
    if n % i == 0:
        print(f"{n} không phải là số nguyên tố")
        break
    else:
        print(f"{n} là số nguyên tố")
        break
