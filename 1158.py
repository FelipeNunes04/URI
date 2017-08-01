n = int(input())
for x in range(1,n+1):
	entrada = input().split()
	x = int(entrada[0])
	y = int(entrada[1])
	cont = 0
	soma = 0
	while cont<y:
		if(x%2!=0):
			soma += x
			cont += 1
		x = x+1
	print(soma)
