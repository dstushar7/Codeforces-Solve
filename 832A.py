# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 04:12:51 2020

@author: dstus
"""

n,k = map(int,input().split())
a = n//k
if (a%2==0):
    print("NO")
else:
    print("YES")