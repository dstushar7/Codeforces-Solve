# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 02:46:54 2020

@author: dstus
"""

m = int(input())
b = 0
for i in range(0,m):
    a = input()
    if a[0]=='+':
        b += 1
    elif a[0]=='-':
        b -= 1
    elif a[1]=='+':
        b += 1
    elif a[1]=='-':
        b -=1
print(b)