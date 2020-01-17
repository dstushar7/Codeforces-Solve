# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 04:15:48 2020

@author: dstus
"""

n,k = map(int,input().split())
d = list(map(int,input().split()))
sum1 = 0
for i in range(0,len(d)):
    for j in range(i+1,len(d)):
        if(((d[i]+d[j])%k)==0):
            sum1 = sum1 + 2
            d.pop(j)
            break
print(sum1)