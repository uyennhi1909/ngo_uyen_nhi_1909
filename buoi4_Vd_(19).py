# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 03:57:24 2024

@author: UNHI
"""

x = float(input("Nhập x = "))

while x < 0:
    x = float(input("Nhập lại x = "))
else:
    print("Giá trị đã nhập:",x)