n = int(input())
produtos = {1001:1.5,1002:2.5,1003:3.5,1004:4.5,1005:5.5}
valor=0
for i in range(n):
	cod,qtd = map(int, input().split())
	valor += produtos[cod]*qtd
print("%.2f"%valor)