# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 10:14:51 2024

@author: UNHI
"""

print("Bộ nghiệm nguyên của phương trình với tổng nghiệm nhỏ nhất là:")
bo_nghiem = []
nhonhat = 979
for x in range(1, 490):  # 2x < 979 nên x < 490
    for y in range(1, 140):  # 7y < 979 nên y < 140
        for z in range(1,109):
            if 2*x + 7*y + 9*z == 979:
                tong = x + y + z 
                if tong < nhonhat:
                    nhonhat = tong
                    bo_nghiem = (x,y,z)
print(f"{bo_nghiem} là bộ nghiệm có tổng nghiệm nhỏ nhất: {bo_nghiem[0]} + {bo_nghiem[1]} + {bo_nghiem[2]} = {nhonhat}")