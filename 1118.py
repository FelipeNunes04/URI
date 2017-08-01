n = 0
sai = 0
mostrarM = 0
media = 0
while mostrarM<2:
	n = float(input())
	if(n<0 or n>10):
		print("nota invalida")
	else:
		media+=n
		mostrarM +=1
	if(mostrarM==2):
		print("media = %.2f"%(media/2))
		while (sai!=2):
			print("novo calculo (1-sim 2-nao)")
			sai = int(input())
			if(sai==2):
				break
			if(sai==1):
				mostrarM=0
				media=0
				break