# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 18:56:19 2020

@author: dstus
"""

m = int(input())
a = str(input())
b = 0
for i in range(1,m):
    if a[i] == a[i-1]:
        b += 1
print(b)