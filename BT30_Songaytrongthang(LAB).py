# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 14:40:48 2024

@author: UNHI
"""
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

if 1 <= thang <= 12 and nam > 0:
    if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
        namnhuan = True
    else:
        namnhuan = False
    ngaytrongthang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if namnhuan: 
        ngaytrongthang[1] = 29 
    print(f"Tháng {thang} năm {nam} có {ngaytrongthang[thang - 1]} ngày ")
