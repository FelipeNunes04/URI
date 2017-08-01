x = float(input())
l = [x]
for i in range(1,100):
	x = x/2
	l.append(x)
for i,v in enumerate(l):
	print("N[%d] = %.4f"%(i,v))