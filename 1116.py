n = int(input())

for i in range (1, n+1):
	n1, n2 = list(map(int, input().split()))

	if (n2 != 0):
		result = float(n1/n2)
		print(result)
	else:
		print("divisao impossivel")