# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 19:12:41 2020

@author: dstus
"""

m = str(input())
m = list(set(m))
m = len(m)
if m%2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")