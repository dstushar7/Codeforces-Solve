# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 02:09:17 2020

@author: dstus
"""

m = int(input())
b = 0
for i in range(0,m):
    a = list(map(int,input().split()))
    c = 0
    for i in range(0,3):
        if a[i]==1:
            c += 1
    if c>=2:
        b += 1
print(b)        