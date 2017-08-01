c = int(input())
if c>=0 and c<12:
	matriz = []
	for i in range(12):
		matriz.append([0]*12)
	op = input()
	soma = 0
	for i in range(0,12):
		for j in range(0,12):
			matriz[i][j] = float(input())
			if(j==c):
				soma += matriz[i][j]
	if op=='S':
		print("%.1f"%soma)
	else:
		print("%.1f"%(soma/12))

