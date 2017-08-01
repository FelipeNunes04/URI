t = int(input())
cont = 0
lista = []
for i in range(0,1000):
	if cont<t:
		lista.append(cont)
	else:
		cont = 0
		lista.append(cont)
	cont += 1
for i,v in enumerate(lista):
	print("N[%d] = %d"%(i,v))

