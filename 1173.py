v = int(input())
if v<=50:
	l = []
	for i in range(0,10):
		l.append(v)
		v*=2
	for i,v in enumerate(l):
		print("N[%d] = %d"%(i,v))