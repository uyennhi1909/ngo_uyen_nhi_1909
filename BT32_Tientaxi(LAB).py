# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 06:08:08 2024

@author: UNHI
"""

distance = float(input("Nhập số km quãng đường đi được: "))
# 1km đầu tiên
if distance <= 1 : 
    tongtien = 15000
# km thứ 2 đến km thứ 5 
elif distance <= 5:
    tongtien = 15000 + 13500*(distance-1) 
# Từ km thứ 6
else:
    tongtien = 15000 + 13500*4 + 11000*(distance-5)
# Giá giảm
if distance > 120: 
    tongtien*=0.9
print(f"Tổng tiền taxi cần trả là {tongtien:.0f}k")