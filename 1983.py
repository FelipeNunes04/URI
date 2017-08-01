num = int(input())
matric,nota=input().split()
notaMaior=float(nota)
matricMaior=matric
for i in range(1,num):
	matric,nota=input().split()
	nota =float(nota)
	if(notaMaior<nota):
		notaMaior = nota
		matricMaior = matric

if(notaMaior<8):
	print("Minimum note not reached")
else:
	print(matricMaior)
