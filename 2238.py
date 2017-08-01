d,nd,m,nm = input().split()
d,nd,m,nm = int(d),int(nd),int(m),int(nm)
resultado = -1
if(d!=nd and m!=nm):
	fim = m
	inicio = d
	while(inicio<=fim):
		if(inicio%d==0 and inicio%nd!=0 and m%inicio==0 and nm%inicio!=0):
			resultado = inicio
			break
		inicio+=d
print(resultado)
