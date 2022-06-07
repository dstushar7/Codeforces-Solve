# Contest: Codeforces Round #797 (Div. 3)

# https://codeforces.com/contest/1690/problem/A

t = int(input())

inputs = []
for i in range(t):
    inputs.append(int(input()))

answer = []
for i in inputs:
    first , second, third = i//3,i//3,i//3
    carry = i%3
    if carry==2:
        first+=2
        second+=1
        third-=1
    elif carry==1:
        if first%2==0:
            first+=2
            second=second
            third-=1
        else:
            first+=2
            second+=1
            third-=2
    else:
        first+=1
        second=second
        third-=1
    answer.append([second,first,third])

for i in answer:
    for x in i:
        print(x, end=" ")
    print()