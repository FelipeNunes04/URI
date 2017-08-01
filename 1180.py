n = int(input())
if n>1 and n<1000:
	vetor = input().split()
	menor = int(vetor[0])
	posi = 0
	for i in range(1,n):
		vetor[i] = int(vetor[i])
		if(vetor[i]<menor):
			menor = vetor[i]
			posi = i

	print("Menor valor: %d"%menor)
	print("Posicao: %d"%posi)