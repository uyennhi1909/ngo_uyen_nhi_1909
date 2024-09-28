# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:19:50 2024

@author: UNHI
"""
n = int(input("Nhập vào số cần tính giai thừa: "))

if n >= 0:
    S = 1
    for i in range(1,n+1):
        S = S*i
    print("Kết quả: ",S)
else:
    print("Nhập lại số nguyên dương")