while True:
    a, d, n = map(int, input().split())
    if a == d == n == 0:
        break

    k = (n - a) / d + 1
    if k % 1 != 0 or k < 1:
        print('X')
    else:
        print(int(k))
