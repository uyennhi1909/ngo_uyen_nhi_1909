# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 06:57:03 2024

@author: UNHI
"""
n = int(input("Nhập vào số nguyên n: "))
while n <= 0 or n % 2 == 0:
    n = int(input("Nhập lại n là số lẻ > 0: "))
else:
    S = 1
    for i in range (1,n+1):
        S*=i
    print("Tổng S là:",S)
