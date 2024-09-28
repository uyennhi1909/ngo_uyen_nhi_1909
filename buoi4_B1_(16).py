# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 13:58:55 2024

@author: UNHI
"""
n = float(input("Nhập một số trong khoảng [-99; 99]: "))

# Sử dụng vòng lặp while để kiểm tra giá trị nhập vào
while n>99 or n<-99:
    n = float(input("Nhập lại một số trong khoảng [-99; 99]: "))
print(f"Số {n} là giá trị hợp lệ")