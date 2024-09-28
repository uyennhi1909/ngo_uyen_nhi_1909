# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:15:22 2024

@author: UNHI
"""
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))
if a+b>c and a+c>b and b+c>a:
    #tam giác đều
    if a ==  b == c:
        print("a,b,c là 3 cạnh của tam giác và đây là tam giác đều")
    #tam giác cân
    elif a == b or a == c or b == c:
        print("a,b,c là 3 cạnh của tam giác và đây là tam giác cân")
    #tam giác vuông
    elif a**2+b**2 == c**2 or a**2+c**2 == b**2 or b**2+c**2 == a**2:
        print("a,b,c là 3 cạnh của tam giác và đây là tam giác vuông")
    else:
        print("a,b,c là 3 cạnh của tam giác")
else:
    print("a,b,c không là 3 cạnh của tam giác")