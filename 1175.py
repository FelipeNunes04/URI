l = []
for i in range(0,20):
	x = int(input())
	l.append(x)
cont = 19
for i in range(0,20):
	if(i<=9):
		aux = l[i]
		l[i] = l[cont]
		l[cont] = aux
		cont-=1
for i,v in enumerate(l):
	print("N[%d] = %d"%(i,v))