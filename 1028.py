num = int(input())
saida = 0
for i in range(num):
	a,b = input().split()
	a,b = int(a),int(b)
	maior,menor = max(a,b),min(a,b)

	while menor>0:
		aux = menor
		menor = maior%menor
		maior = aux

	print(maior)
