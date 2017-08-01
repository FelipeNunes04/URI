n = int(input())
for i in range(0,n):
	x = int(input())
	soma = 0
	perfeito = False
	for j in range(1,x):
		if(x%j==0):
			soma += j
	if(soma == x):
		print("%d eh perfeito"%x)
	else:
		print("%d nao eh perfeito"%x)
