# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:08:31 2024

@author: UNHI
"""

thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

if 1 <= thang <= 12 and nam > 0:
    if thang in {1,3,5,7,8,10,12}:
        ngay = 31
    elif thang == 2:
        if (nam % 4 == 0 and nam % 100 != 0) or nam % 400:
            ngay = 29
        else:
            ngay = 28
    else:
        ngay = 30
    print(f"Thang {thang} năm {nam} có {ngay} ngày")
else:
    print("Tháng năm không hợp lệ")