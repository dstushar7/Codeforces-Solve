# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 03:02:44 2020

@author: dstus
"""

for i in range(0,5):
    a = list(map(int,input().split()))
    for j in range(0,5):
        if a[j]==1:
            b = j+1
            c = i+1
            d = abs(3-b)+abs(3-c)
print(d)   