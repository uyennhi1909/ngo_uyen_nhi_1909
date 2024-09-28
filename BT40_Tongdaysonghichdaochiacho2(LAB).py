# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 07:29:27 2024

@author: UNHI
"""

n = int(input("Nhập vào số nguyên n: "))
while n < 0:
    n = int(input("Nhập lại n là số nguyên dương: "))
else:
    S = 0
    for i in range (1,n+1):
        S+=1/(2*i)
    print("Tổng S là:",S)