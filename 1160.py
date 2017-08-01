n = int(input())
if n>0 and n<=3000:
	for i in range(0,n):
		entrada = input().split()
		pa = int(entrada[0])
		pb = int(entrada[1])
		cont = 0
		percPa = float(entrada[2])
		percPb = float(entrada[3])
		while pa<=pb:
			cont+=1
			if cont>100:
				break
			else:
				pa += int((pa*(percPa/100)))
				pb += int((pb*(percPb/100)))
		if cont>100:
			print("Mais de 1 seculo.")
		else:
			print("%d anos."%cont)
			