a,c = input().split()
a = int(a)
negA = a*-1
canos = input().split()
lista_canos = []
for i in canos:
	i = int(i)
	lista_canos.append(i)
for i in range(len(lista_canos)-1):
	if((lista_canos[i+1]-lista_canos[i])>a or (lista_canos[i+1]-lista_canos[i])<negA):
		ganhou = False
		break
	else:
		ganhou = True

if(ganhou):
	print("YOU WIN")
else:
	print("GAME OVER")	

