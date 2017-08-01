m = 1
n = 1
while(n>0 and m>0):
	soma = 0
	saida = ""
	entrada = input().split()
	m = int(entrada[0])
	n = int(entrada[1])
	if(n<1 or m<1 ):
		break;
	elif(n<m):
		for i in range(n,m+1):
			soma +=i
			saida = saida+(str(i)+" ")
	elif(m<n):
		for i in range(m,n+1):
			soma +=i
			saida = saida+(str(i)+" ")
	print(saida+"Sum=%d"%soma)