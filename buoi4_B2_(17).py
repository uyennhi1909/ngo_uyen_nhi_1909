# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:39:17 2024

@author: UNHI
"""

n = float(input("Nhập một số trong khoảng [-89.9; 88.8]: "))

# Sử dụng vòng lặp while để kiểm tra giá trị nhập vào
while n>88.8 or n<-89.9:
    n = float(input("Nhập lại một số trong khoảng [-89.9; 88.8]: "))
print(f"Số {n} là giá trị hợp lệ")