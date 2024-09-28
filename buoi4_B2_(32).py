# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:24:58 2024

@author: UNHI
"""

# Tạo danh sách các số chẵn từ 2018 đến 3838
numbers = [0] * ((3838 - 2018) // 2 + 1)  # Khởi tạo danh sách với kích thước phù hợp
id = 0

for i in range(2020, 3839):
    if i % 2 == 0:
        numbers[id] = i
        id = id + 1

# Tạo danh sách các số chia hết cho 9
chia_9 = [0] * (id)  # Khởi tạo danh sách với kích thước tối đa
id_9 = 0

for num in numbers:
    if num != 0 and num % 9 == 0:  # Kiểm tra các số hợp lệ
        chia_9[id_9] = num
        id_9 = id_9 + 1

# In các số thu được thành chuỗi, cách nhau bằng 1 tab
for i in range(id_9):
    print(chia_9[i], end='\t')  # Thêm tab giữa các số