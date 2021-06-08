line = input().split(" ")

a, b, c = line

def maior(a, b):
	maior = (int(a) + int(b) + abs(int(a)-int(b)))/2
	return maior

result = maior(a, b)
result_fin = maior(result, c)

print("%d eh o maior" % result_fin)