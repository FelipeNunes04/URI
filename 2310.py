n = int(input())
somSacTent, somSacSuss = 0,0
somBlocTent, somBlocSuss = 0,0
somAtacTent, somAtacSuss = 0,0
for i in range(n):
	nome = input()
	entTentativas = list(map(int, input().split()))
	entSucesso = list(map(int, input().split()))
	somSacTent += entTentativas[0] 
	somBlocTent += entTentativas[1]
	somAtacTent += entTentativas[2]

	somSacSuss += entSucesso[0] 
	somBlocSuss += entSucesso[1]
	somAtacSuss += entSucesso[2]

percSac = somSacSuss/somSacTent*100
percBloc = somBlocSuss/somBlocTent*100
percAtac = somAtacSuss/somAtacTent*100

print("Pontos de Saque: %.2f %%."%percSac)
print("Pontos de Bloqueio: %.2f %%."%percBloc)
print("Pontos de Ataque: %.2f %%."%percAtac)


