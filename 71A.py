# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 05:41:15 2020

@author: dstus
"""
m = int(input())
a = []
for i in range(0,m):
    b = input()
    a.append(b)
for i in range(0,m):
    if len(a[i])>10:
        print(str(a[i][0]+(str(len(a[i])-2))+a[i][-1]))
    else:
        print(str(a[i]))