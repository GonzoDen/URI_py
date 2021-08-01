nums = [6,2,5,5,4,5,6,3,7,6]
n = int(input())

for i in range(n):
    leds = 0
    num = input()

    for j in num:
        leds += nums[int(j)]

    print("%d leds" % int(leds))
