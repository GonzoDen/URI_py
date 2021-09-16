def find_biggest(days):
    cur_max = new_max = days[0]
    for i in days[1:]:
        cur_max = max(i, cur_max + i)
        new_max = max(new_max, cur_max)
    return new_max

while True:
    try:
        n = int(input())
        cost = int(input())
        days = []
        for i in range(n):
            days.append(int(input()) - cost)
        res = find_biggest(days)
        if res < 0:
            res = 0
        print(res)

    except EOFError:
        break