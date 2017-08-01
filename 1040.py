notas = list(map(float, input().split()))
media = (notas[0]*2+notas[1]*3+notas[2]*4+notas[3]*1)/10
if media>=7:
	print("Media: %.1f"%media)
	print("Aluno aprovado.")
elif media>=5:
	print("Media: %.1f"%media)
	print("Aluno em exame.")
	nota_exame = float(input())
	media_final = (media+nota_exame)/2
	print("Nota do exame: %.1f"%nota_exame)
	if media_final>=5:
		print("Aluno aprovado.")
	else:
		print("Aluno reprovado.")
	print("Media final: %.1f"%media_final)
else:
	print("Media: %.1f"%media)
	print("Aluno reprovado.")