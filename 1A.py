# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 04:37:54 2020

@author: dstus
"""

import math
n,m,a = map(int,input().split())
b = math.ceil(n/a)#To round up a number
c = math.ceil(m/a)
print(b*c)