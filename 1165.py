n = int(input())
for i in range(0,n):
	x = int(input())
	cont = 0
	for j in range(1,x):
		if(x%j==0):
			cont+=1
	if(cont>1):
		print("%d nao eh primo"%x)
	else:
		print("%d eh primo"%x)