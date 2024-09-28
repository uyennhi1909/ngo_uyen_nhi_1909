# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 09:50:45 2024

@author: UNHI
"""
print("Bộ nghiệm nguyên của phương trình là:")
bo_nghiem = []
for x in range(1, 490):  # 2x < 979 nên x < 490\
    for y in range(1, 140):  # 7y < 979 nên y < 140
        for z in range(1,109):
            if 2*x + 7*y + 9*z == 979:
                bo_nghiem += [(x,y,z)]
print(bo_nghiem)