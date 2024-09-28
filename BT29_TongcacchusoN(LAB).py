# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:26:38 2024

@author: UNHI
"""

n = int(input("Nhập số N: "))
tong = 0

while n <= 0 :
    n = int(input("Nhập lại số N là số nguyên dương: "))
while n > 0:
    tong = tong + n % 10
    n = n//10
print(f"Tổng các chữ số N là: {tong}")