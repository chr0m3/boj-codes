secs = int(input())

if secs % 10 != 0:
    print(-1)
else:
    a = secs // 300
    secs %= 300
    b = secs // 60
    secs %= 60
    c = secs // 10
    print(f'{a} {b} {c}')
