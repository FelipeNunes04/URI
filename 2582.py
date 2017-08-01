musics = ["PROXYCITY","P.Y.N.G.","DNSUEY!","SERVERS","HOST!",
	"CRIPTONIZE","OFFLINE DAY","SALT","ANSWER!","RAR?","WIFI ANTENNAS"]
n = int(input())

for i in range(n):
	a,b = map(int, input().split())
	print(musics[a+b])