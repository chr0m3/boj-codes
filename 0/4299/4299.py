a, b = map(int, input().split())

c = (a + b) / 2
d = (a - b) / 2

if c % 1 != 0 or d % 1 != 0 or c < 0 or d < 0:
    print(-1)
else:
    print(f'{int(c)} {int(d)}')
