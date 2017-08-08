while True:
	try:
		h,m = map(int,input().split(":"))
		minutos = h*60+m+60
		if(minutos>480):
			atraso = minutos-480
			print("Atraso maximo: %d"%atraso)
		else:
			print("Atraso maximo: 0")
	except EOFError:
		break