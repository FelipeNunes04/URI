lista = []
for i in range(0,100):
	x = float(input())
	lista.append(x)
for i,v in enumerate(lista):
	if(v<=10):
		print("A[%d] = %.1f"%(i,v))