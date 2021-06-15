N_RANGE = 6

n = int(input())

for i in range(N_RANGE*2):
	if n % 2 != 0:
		print(n)
	n += 1