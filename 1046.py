line1 = input().split(" ")

h1, h2 = line1

if h1 <= h2:
	result = 24 - (int(h1)-int(h2))
	print("O JOGO DUROU %d HORA(S)" % result)
else:
	print("O JOGO DUROU %d HORA(S)" % (int(h2)-int(h1)))