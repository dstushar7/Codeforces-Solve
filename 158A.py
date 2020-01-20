# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 05:48:25 2020

@author: dstus
"""
#158A
m,n = map(int, input().split())
a = list(map(int, input().split()))
b = 0
c = a[n-1]
for i in range(0,m):
    if a[i]!=0:
        if a[i]>=c:
            b += 1
print(b)