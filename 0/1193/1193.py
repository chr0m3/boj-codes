x = int(input())

n = 1
while True:
    if x <= n * (n + 1) / 2:
        m = int(x - ((n - 1) * n / 2))
        break
    n += 1

if n % 2 == 0:
    print(f'{m}/{n - m + 1}')
else:
    print(f'{n - m + 1}/{m}')
