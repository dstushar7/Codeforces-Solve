# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 04:14:23 2020

@author: dstus
"""

n,k = map(int,input().split())
q = 0
m = 0
if k!=0:
    q = n//k
    m = n%k

if  ((q==1) & (m==0)):
    print('0 0')
elif((q==1) & (m>0)):
    print('1 '+str(m))
elif((q==2) & (m==0)):
    print('1 '+str(k))
elif((q==2) & (m>0)):
    print('1 '+str(k+m))
elif(q>=3):
    print('1 '+str(k*2))
else:
    print('0 0')