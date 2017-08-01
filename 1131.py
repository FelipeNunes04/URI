op = 0
empate = 0
inter = 0
gremio = 0
grenais = 0
while op!=2:
	op = 0
	entrada = input().split()
	gInter = int(entrada[0])
	gGremio = int(entrada[1])
	if(gInter==gGremio):
		empate+=1 
	elif(gInter>gGremio):
		inter+=1
	else:
		gremio+=1
	while op!=2 and op!=1:
		print("Novo grenal (1-sim 2-nao)")
		op = int(input())
	grenais+=1
print("%d grenais"%grenais)
print("Inter:%d"%inter)
print("Gremio:%d"%gremio)
print("Empates:%d"%empate)
if(inter>gremio):
	print("Inter venceu mais")
elif(gremio>inter):
	print("Gremio venceu mais")
else:
	print("Nao houve vencedor")