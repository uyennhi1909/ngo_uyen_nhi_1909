# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 07:38:10 2024

@author: UNHI
"""


n = int(input("Nhập vào số nguyên n: "))
while n < 0:
    n = int(input("Nhập lại n là số nguyên dương: "))
else:
    S = 0
    for i in range (1,n+1):
        S+=1/(i*(i+1))
    print("Tổng S là:",S)