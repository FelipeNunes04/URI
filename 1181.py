
l = int(input())
if l>=0 and l<12:
	matriz = []
	for i in range(12):
		matriz.append([0]*12)
	op = input()
	soma = 0
	for i in range(0,12):
		for j in range(0,12):
			matriz[i][j] = float(input())
			if(i==l):
				soma += matriz[i][j]
	if op=='S':
		print(soma)
	else:
		print("%.1f"%(soma/12))

