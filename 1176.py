l = []
a,b,c = 0,1,1
for i in range(0,61):
	l.append(a)
	a = b
	b = c
	c = a+b
t = int(input())
for i in range(0,t):
	n = int(input())
	if(n>=0 and n<=60):
		print("Fib(%d) = %d"%(n,l[n]))
