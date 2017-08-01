while True:
	n = int(input())
	if n==0:
		break
	matriz = []
	for i in range(n):
		matriz.append(n*[0])
	
	for i in range(n):
		for j in range(n):
			x = min(i+1,n-i)
			y = min(j+1,n-j)
			matriz[i][j] = min(x,y)
	for i in range(n):
		for j in range(n):
			print("%3d"%matriz[i][j],end="")
			if(j<(n-1)):
				print(" ",end="")
		print("")
	print("")