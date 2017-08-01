#	Autor: Felipe Nunes
#	Data: 13/09/2016

n = int(input())
c = 0
r = 0
s = 0
total = 0
for x in range(n):
	cobaia = input().split()
	nCobaias = int(cobaia[0])
	if nCobaias>0 and nCobaias<=15:
		total += nCobaias
		if cobaia[1] == "C":
			c += nCobaias
		elif cobaia[1] == "R":
			r += nCobaias
		else:
			s += nCobaias

perc_c = float((c/total)*100)
perc_r = float((r/total)*100)
perc_s = float((s/total)*100)
print("Total: %d cobaias"%total)
print("Total de coelhos: %d"%c)
print("Total de ratos: %d"%r)
print("Total de sapos: %d"%s)
print("Percentual de coelhos: %.2f %%"%perc_c)
print("Percentual de ratos: %.2f %%"%perc_r)
print("Percentual de sapos: %.2f %%"%perc_s)