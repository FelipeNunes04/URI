while True:
	try:
		n = int(input())
		nums = list(map(int,input().split()))
		a_favor = nums.count(1)
		if(a_favor>=n*(2/3)):
			print("impeachment")
		else:
			print("acusacao arquivada")
	except EOFError:
		break