m = int(input())
a = list(map(int,input().split()))
p = 0
m = 0
n = 0
o = 0
for i in a:
	if i==1:
		p += 1
	elif i==2:
		o += 1
	elif i==3:
		n += 1
	elif i==4:
		m += 1
x = int(p/4)+int(o/2)+m
p %= 4
o %= 2
while p != 0 and n !=0:
	p -= 1
	n -= 1
	x += 1
if n != 0:
	x += n
