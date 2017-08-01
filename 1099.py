n = int(input())
for i in range(0,n):
	somaInteiros = 0
	entrada = input().split()
	x = int(entrada[0])
	y = int(entrada[1])
	if(x<y):
		for j in range(x+1,y):
			if(j%2!=0):
				somaInteiros += j
	elif(y<x):
		for j in range(y+1,x):
			if(j%2!=0):
				somaInteiros += j
	print(somaInteiros)

