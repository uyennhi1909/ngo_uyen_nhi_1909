# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 12:54:48 2024

@author: UNHI
"""

# Tạo danh sách các số chẵn từ 2018 đến 2828
numbers = [0] * ((2828 - 2018) // 2 + 1)  # Khởi tạo danh sách với kích thước phù hợp
id = 0

for i in range(2018, 2829):
    if i % 2 == 0 and i % 5 == 0:
        numbers[id] = i
        id = id + 1
for i in range(id):
    print(numbers[i], end='\t')  # Thêm tab giữa các số

