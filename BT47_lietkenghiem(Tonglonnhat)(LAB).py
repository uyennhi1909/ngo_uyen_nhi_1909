# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 10:02:49 2024

@author: UNHI
"""
print("Bộ nghiệm nguyên của phương trình với tổng nghiệm lớn nhất là:")
bo_nghiem = []
lonnhat = 0
for x in range(1, 490):  # 2x < 979 nên x < 490
    for y in range(1, 140):  # 7y < 979 nên y < 140
        for z in range(1,109):
            if 2*x + 7*y + 9*z == 979:
                tong = x + y + z 
                if tong > lonnhat:
                    lonnhat = tong
                    bo_nghiem = (x,y,z)
print(f"{bo_nghiem} là bộ nghiệm có tổng nghiệm lớn nhất: {bo_nghiem[0]} + {bo_nghiem[1]} + {bo_nghiem[2]} = {lonnhat}")