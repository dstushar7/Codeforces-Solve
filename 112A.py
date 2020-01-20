# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 02:47:42 2020

@author: dstus
"""

a = str(input())
b = str(input())
a = a.lower()
b = b.lower()
if a==b:
    print('0')
elif a>b:
    print('1')
else:
    print('-1')