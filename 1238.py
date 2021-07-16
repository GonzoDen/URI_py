n = int(input())

for i in range(n):
    line = input().split(" ")
    w1,w2 = line

    w = ''

    if(len(w1) <= len(w2)):
        for i in range(len(w1)):
            w += w1[i]
            w += w2[i]
        w += w2[len(w1):]

    else:
        for i in range(len(w2)):
            w += w1[i]
            w += w2[i]
        w += w1[len(w2):]

    print(w)