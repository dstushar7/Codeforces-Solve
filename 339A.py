# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 04:01:41 2020

@author: dstus
"""

a = list(input())#Inputting as string
x = []
y = []
z = []
for i in range(0,len(a)):#checking how many 1,2,3's
    if(a[i]=='1'):
        x.append('1')
    elif(a[i]=='2'):
        y.append('2')
    elif(a[i]=='3'):
        z.append('3')
xyz = x+y+z
a = '+'.join(str(e) for e in xyz)
print(a)