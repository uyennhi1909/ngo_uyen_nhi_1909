# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 06:51:18 2024

@author: UNHI
"""

n = int(input("Nhập vào số nguyên n: "))
while n <= 0 or n % 2 != 0:
    n = int(input("Nhập lại n là số chẵn > 0: "))
else:
    S = 0
    for i in range (2,n+1,2):
        S+=i
    print("Tổng S là:",S)