o = input()
matriz = []
for i in range(12):
	matriz.append([0]*12)
soma = 0
cont = 0
for i in range(12):
	for j in range(12):
		matriz[i][j] = float(input())
		if i+j>11 and i < j:
			soma+=matriz[i][j]
			cont+=1


if(o=='S'):
	print("%.1f"%soma)
else:
	print("%.1f"%(soma/cont))
