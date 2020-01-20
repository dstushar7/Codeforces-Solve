# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 03:43:09 2020

@author: dstus
"""

a = str(input())
a = a.lower()
b = []
for i in a:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='y':
        continue
    else:
        b.append('.'+i)
c = ''.join(str(e) for e in b)
print(c)