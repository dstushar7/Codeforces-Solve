# Contest: Codeforces Round #797 (Div. 3)

# https://codeforces.com/contest/1690/problem/C

# C- Restoring the Duration of Tasks

t = int(input())
for hululu in range(t):
    n = int(input())
    start =[int(x) for x in input().split()]
    end =[int(x) for x in input().split()]
    answer = []
    answer.append(end[0]-start[0])
    for i in range(1,n):
        answer.append(end[i]-max(end[i-1],start[i]))
    for i in answer:
        print(i, end=" ")
    print()