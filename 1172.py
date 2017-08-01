lista = []
for i in range(0,10):
	x = int(input())
	if x>0:	
		lista.append(x)
	else:
		lista.append(1)
for i,v in enumerate(lista):
	print("X[%d] = %d"%(i,v))

	