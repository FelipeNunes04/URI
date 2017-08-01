n = int(input())
for i in range(n):
	entrada = input().split()
	num = entrada[0]
	tipo = entrada[1]
	if(tipo=="bin"):
		dec = int(num,2)
		hexa = hex(dec)
		hexa = hexa[2:]
		print("Case %d:"%(i+1))
		print("%s dec"%(dec))
		print("%s hex\n"%(hexa))
	elif(tipo=="dec"):
		num = int(num)
		bina = bin(num)
		bina = bina[2:]
		hexa = hex(num)
		hexa = hexa[2:]
		print("Case %d:"%(i+1))
		print("%s hex"%(hexa))
		print("%s bin\n"%(bina))
	else:
		dec = int(num,16)
		bina = bin(dec)
		bina = bina[2:]
		print("Case %d:"%(i+1))
		print("%s dec"%(dec))
		print("%s bin\n"%(bina))