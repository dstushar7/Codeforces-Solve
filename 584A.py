# -*- coding: utf-8 -*-
n,t = map(int,input().split())
d = 0
c = 10**(n-1)
if (n==1 & t==10):
        print(-1)
else:
    for i in range(0,9):
        if (c%t)== 0:
            print(c)
            d = 1
            break
        else: 
            c+=1
    if (d == 0):
        print("-1")