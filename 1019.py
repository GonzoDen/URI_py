secs = int(input())

mins = int(secs / 60)
secs %= 60
hours = int(mins / 60)
mins %= 60


print(f'{hours}:{mins}:{secs}')