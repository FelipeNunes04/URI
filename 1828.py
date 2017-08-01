n = int(input())
for i in range(n):
	entrada = input().split()
	if entrada[0] == entrada[1]:
		print("Caso #%d: De novo!"%(i+1))
	elif (entrada[0]=="tesoura" and entrada[1]=="papel") or (entrada[0]=="papel" and entrada[1]=="pedra") or (entrada[0]=="pedra" and entrada[1]=="lagarto") or (entrada[0]=="lagarto" and entrada[1]=="Spock") or (entrada[0]=="Spock" and entrada[1]=="tesoura") or (entrada[0]=="tesoura" and entrada[1]=="lagarto") or (entrada[0]=="lagarto" and entrada[1]=="papel") or (entrada[0]=="papel" and entrada[1]=="Spock") or (entrada[0]=="Spock" and entrada[1]=="pedra") or (entrada[0]=="pedra" and entrada[1]=="tesoura"):
		print("Caso #%d: Bazinga!"%(i+1))
	elif (entrada[1]=="tesoura" and entrada[0]=="papel") or (entrada[1]=="papel" and entrada[0]=="pedra") or (entrada[1]=="pedra" and entrada[0]=="lagarto") or (entrada[1]=="lagarto" and entrada[0]=="Spock") or (entrada[1]=="Spock" and entrada[0]=="tesoura") or (entrada[1]=="tesoura" and entrada[0]=="lagarto") or (entrada[1]=="lagarto" and entrada[0]=="papel") or (entrada[1]=="papel" and entrada[0]=="Spock") or (entrada[1]=="Spock" and entrada[0]=="pedra") or (entrada[1]=="pedra" and entrada[0]=="tesoura"):
		print("Caso #%d: Raj trapaceou!"%(i+1))
