for _ in range(3):
    ha, ma, sa, hb, mb, sb = map(int, input().split())

    secs = (hb * 3600 + mb * 60 + sb) - (ha * 3600 + ma * 60 + sa)

    h = secs // 3600
    secs %= 3600
    m = secs // 60
    secs %= 60
    s = secs

    print(f'{h} {m} {s}')
