n = int(input())

for t in range(n):
    m = (n + 1) // 2
    l = n - m
    for _ in range(m):
        print('* ', end='')
    if l:
        print()
    for _ in range(l):
        print(' *', end='')
    if t != (n - 1):
        print()
