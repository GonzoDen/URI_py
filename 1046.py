h1, h2 = list(map(int,input().split()))

if(h1 < h2):
    result = h2 - h1
else:
    result = h2 + 24 - h1

print(f"O JOGO DUROU {result} HORA(S)")