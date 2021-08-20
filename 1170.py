n = int(input())

for i in range(n):
	count = 0
	num = float(input())
	while (num > 1):
		num /=2
		count += 1
	print("%d dias" % count)
