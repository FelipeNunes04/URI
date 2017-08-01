a,b,c,d = input().split()
a,b,c,d = int(a),int(b),int(c),int(d)
lista = [a,b,c,d]
if(a==b==c==d):
	print("S")
else:
	for i in range(len(lista)):
		j = i
		while(j<len(lista)):
			if(lista[i]>lista[j]):
				aux = lista[i]
				lista[i] = lista[j]
				lista[j] = aux
			j+=1
	if (lista[0]+lista[1])>lista[2]:
		print("S")
	elif (lista[1]+lista[2]) > lista[3]:
		print("S")
	else:
		print("N")
