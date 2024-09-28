# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:54:16 2024

@author: UNHI
"""

n = int(input("Nhập vào số N: "))
while n<=0:
    n = int(input("Nhập lại số N: "))
for i in range(1,n+1):
    if n % i == 0:
        print(i)
