n = int(input())

for i in range(1, n + 1):
    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)

for i in range(1, n):
    print('*' * (n - i) + ' ' * (2 * i) + '*' * (n - i))
