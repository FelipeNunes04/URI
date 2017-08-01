frutas = {"suco de laranja": 120,"morango fresco":85, "mamao":85,"goiaba vermelha":70,
	"manga":56,"laranja":50,"brocolis":34}
while True:
	n = int(input())
	if(n==0):
		break
	vitamina = 0
	for i in range(n):
		entrada = input().split()
		qtd = int(entrada[0])
		fruta = " ".join(entrada[1:])
		vitamina+=frutas[fruta]*qtd
	if(vitamina>130):
		print("Menos %d mg"%(vitamina-130))
	elif(vitamina<110):
		print("Mais %d mg"%(110-vitamina))
	else:
		print("%d mg"%vitamina)