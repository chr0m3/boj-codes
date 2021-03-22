n = int(input())

for i in range(1, n+1):
    print(('*' * i).rjust(n))

for i in range(1, n):
    print((('*' * (n - i)).rjust(n)))
