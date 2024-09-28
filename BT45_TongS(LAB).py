# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 10:29:56 2024

@author: UNHI
"""
x = float(input("Nhập giá trị của x: "))
n = int(input("Nhập vào số nguyên n: "))
while n < 0:
    n = int(input("Nhập lại n là số nguyên dương: "))
else:
    S = 0
    mau = 0 
    tu = 0
    for i in range (1,n+1):
        tu = x**i
        mau += i
        S= S + (tu/mau)
    print(f"Tổng S là: {S:}")