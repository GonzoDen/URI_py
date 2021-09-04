while True:
    try:
        v, t = map(int, input().split())
        res = v*2*t
        print(res)

    except EOFError:
            break