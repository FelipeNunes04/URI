o = input()
matriz = []
for i in range(12):
	matriz.append([0]*12)
soma = 0
cont = 11
for i in range(12):
	for j in range(12):
		matriz[i][j] = float(input())
		if j>cont:
			soma+=matriz[i][j]
	cont-=1

if(o=='S'):
	print("%.1f"%soma)
else:
	print("%.1f"%(soma/66))
