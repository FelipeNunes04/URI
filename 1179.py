contI,contP = 0,0
pares,impares = [],[]
for i in range(0,15):
	x = int(input())
	if x%2==0:
		pares.append(x)
		contP+=1
	else:
		impares.append(x)
		contI+=1
	if contP==5:
		contP = 0
		for ind,v in enumerate(pares):
			print("par[%d] = %d"%(ind,v))
		pares = []
	if contI==5:
		contI = 0
		for ind,v in enumerate(impares):
			print("impar[%d] = %d"%(ind,v))
		impares = []
	if i == 14:
		for ind,v in enumerate(impares):
			print("impar[%d] = %d"%(ind,v))
		for ind,v in enumerate(pares):
			print("par[%d] = %d"%(ind,v))
		break