# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 04:15:06 2020

@author: dstus
"""
n = int(input())
k = input()
d=[]
c = list(k)
for i in range(0,n//2):
    d.append(c[(n-1)-(i*2+1)])
if(n%2==0):
    for i in range(0,n//2):
        d.append(c[(i*2+1)])
else:
    for i in range(0,n//2+1):
        d.append(c[(i*2)])
ans = ''.join(d)
print(ans)