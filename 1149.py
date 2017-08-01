entrada = list(map(int, input().split()))
a = entrada[0]
n = entrada[len(entrada)-1]

soma=0
for i in range(a,a+n):
	soma+=i
print(soma)