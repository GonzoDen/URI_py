n = int(input())

l = list(map(int, input().split()))

minim = l[0]
pos = 0
count = 0

for i in l:
	if i < minim:
		minim = i
		pos = count
	count += 1

print("Menor valor: %d" % minim)
print("Posicao: %d" % pos)