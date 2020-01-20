# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 02:50:04 2020

@author: dstus
"""
a = str(input())
c = 1
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        c += 1
    else:
        c = 1
    if c==7:
        print('YES')
        break
if c!=7:
    print('NO')