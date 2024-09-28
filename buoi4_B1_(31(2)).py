# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:35:38 2024

@author: UNHI
"""

n = int(input("Nhập số N: "))
tong = 0

while n <= 0 :
    n = int(input("Nhập lại số N là số nguyên dương: "))
tong = 0
for i in range(1,n+1):
    tong+= n%10
    n//=10
print(f"Tổng các chữ số N là: {tong}")