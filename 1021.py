valor_notas = float(input())

nCem = int(valor_notas/100)
valor_notas = valor_notas%100
nCinq = int(valor_notas/50)
valor_notas = valor_notas%50
nVint = int(valor_notas/20)
valor_notas = valor_notas%20
nDez = int(valor_notas/10)
valor_notas = valor_notas%10
nCinc = int(valor_notas/5)
valor_notas = valor_notas%5
nDois = int(valor_notas/2)
valor_notas = valor_notas%2

valor_notas = round(valor_notas,2)

valor_moedas = valor_notas*100

mUm = int(valor_moedas/100)
valor_moedas = valor_moedas%100
mCinq = int(valor_moedas/50)
valor_moedas = valor_moedas%50
mVintCinc = int(valor_moedas/25)
valor_moedas = valor_moedas%25
mDez = int(valor_moedas/10)
valor_moedas = valor_moedas%10
mCinc = int(valor_moedas/5)
valor_moedas = valor_moedas%5

print("NOTAS:")
print("%d nota(s) de R$ 100.00"%nCem)
print("%d nota(s) de R$ 50.00"%nCinq)
print("%d nota(s) de R$ 20.00"%nVint)
print("%d nota(s) de R$ 10.00"%nDez)
print("%d nota(s) de R$ 5.00"%nCinc)
print("%d nota(s) de R$ 2.00"%nDois)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00"%valor_notas)
print("%d moeda(s) de R$ 0.50"%mCinq)
print("%d moeda(s) de R$ 0.25"%mVintCinc)
print("%d moeda(s) de R$ 0.10"%mDez)
print("%d moeda(s) de R$ 0.05"%mCinc)
print("%d moeda(s) de R$ 0.01"%valor_moedas)