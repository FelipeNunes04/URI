import math
a = 1
while(a!=0):
	entrada = input().split()
	a = int(entrada[0])
	if(a==0):
		break
	b = int(entrada[1])
	c = int(entrada[2])
	saida = (a*b)*(100/c)
	saida = int(math.sqrt(saida))
	print(saida)