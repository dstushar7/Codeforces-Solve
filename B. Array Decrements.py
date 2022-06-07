# Contest: Codeforces Round #797 (Div. 3)

# https://codeforces.com/contest/1690/problem/B

# B. Array Decrements # Solved



t = int(input())

for blahblah in range(t):
    n = int(input())
    a =[int(x) for x in input().split()]
    b =[int(x) for x in input().split()]
    c = set() 

    temp_zero = -1

    flag = 0
    if (sum(b)==0):
        flag=1
    else:
        for i in range(n):
            difference = a[i]-b[i]
            if difference<0:
                flag = 0
                break
            if b[i]==0:
                if(difference>=temp_zero):
                    temp_zero=difference
            else:
                c.add(difference)
                if len(c)>1:
                    flag = 0
                    break
            flag = 1
        if len(c)!=0:    
            if(list(c)[0]<temp_zero):
                flag = 0
    if(flag==1):
        print("YES")
    else:
        print("NO")