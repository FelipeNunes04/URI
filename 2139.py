while True:
	try:
		mes,dia = map(int, input().split())
		if(dia==25 and mes==12): print("E natal!")
		elif(dia==24 and mes==12): print("E vespera de natal!")
		elif(dia>25 and mes==12): print("Ja passou!")
		else:
			dias = [31,29,31,30,31,30,31,31,30,31,30,25]
			soma = 0-dia
			for i in range(mes-1,12):
				soma+=dias[i]
			print("Faltam %d dias para o natal!"%soma)
	except EOFError:
		break
