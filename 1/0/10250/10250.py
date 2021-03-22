cases = int(input())

for i in range(cases):
    h, w, n = map(int, input().split())
    n -= 1
    print(f'{n % h + 1}{str(n // h + 1).zfill(2)}')
