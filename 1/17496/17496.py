n, t, c, p = map(int, input().split())

counts = (n - 1) // t
print(counts * c * p)
