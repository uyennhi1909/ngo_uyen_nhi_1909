# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 08:24:09 2024

@author: UNHI
"""

S_le = 0
S_chan = 0
for i in range(101):
    if i % 2 == 0 :
        S_chan+=i
    else:
        S_le+=i
print(f"Tổng các số chẵn là: {S_chan}")
print(f"Tổng các số lẻ là: {S_le}")