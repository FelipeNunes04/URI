o = input()
matriz = []
for i in range(12):
	matriz.append([0]*12)
soma = 0
cont1 = 11
cont2 = 0
for i in range(12):
	for j in range(12):
		matriz[i][j] = float(input())
		if j<cont1 and j>cont2:
			soma+=matriz[i][j]
	cont1-=1
	cont2+=1

if(o=='S'):
	print("%.1f"%soma)
else:
	print("%.1f"%(soma/30))
