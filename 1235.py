n = int(input())

while(n > 0):
    n -= 1
    line = input()
    mid = int(len(line)/2) - 1
    res = line[mid::-1] + line[len(line)-1:mid:-1] 
    #the line above is the reason I love Python
    print(res)