n = int(input())
lista_nums = [900,500,400,100,90,50,40,10,9,5,4,1]
lista_roms = ['CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
resultado = ''
for i in range(len(lista_nums)):
	cont = int(n/lista_nums[i])
	resultado+=lista_roms[i]*cont
	n -= lista_nums[i]*cont
	if n==0:
		break
print(resultado) 