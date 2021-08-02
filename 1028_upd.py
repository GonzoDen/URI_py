def noz(n1, n2):
	ost = None #NULL value, original/empty state (datatype), do not confuse with empty string, False, or 0
	while ost != 0:
		ost = n1 % n2
		n1 = n2
		n2 = ost
	return n1


n = int(input())

for i in range(n):
	n1, n2 = list(map(int, input().split(" ")))
	print(noz(n1, n2))