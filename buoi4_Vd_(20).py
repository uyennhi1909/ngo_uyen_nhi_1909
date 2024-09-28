# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 04:01:21 2024

@author: UNHI
"""

count = 0 
n = int(input("Nhập vào số lần cần lặp: "))
while (count < n) :
    print("Lần lặp thứ: ", count + 1,"\tBiến đếm:", count)
    count = count + 1
else:
    print("\nThực hiện lệnh trong else, do:",
          "\ncount = ",count,"\nn = ",n,
          "\nbool(count < n) = ",bool(count<n))