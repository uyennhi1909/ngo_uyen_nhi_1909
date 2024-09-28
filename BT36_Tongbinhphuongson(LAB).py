# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 06:49:55 2024

@author: UNHI
"""

n = int(input("Nhập vào số nguyên n: "))
while n <= 0:
    n = int(input("Vui lòng nhập lại số nguyên dương n: "))
else:
    S = 0
    for i in range (1,n+1):
        S = S+i**2
    print("Tổng S là:",S)