# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 19:12:53 2020

@author: dstus
"""

m = int(input())
x = 0
y = 0
z = 0
for i in range(0,m):
    a,b,c = map(int,input().split())
    x += a
    y += b
    z += c
if x==0 and y==0 and z==0:
    print("YES")
else:        
    print("NO")