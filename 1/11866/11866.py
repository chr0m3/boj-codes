n, k = map(int, input().split())

circle = [x for x in range(1, n + 1)]
series = list()
target = 0
for i in range(n):
    target = (target + k - 1) % (n - i)
    series.append(circle[target])
    circle = circle[:target] + circle[target + 1:]

print(f"<{', '.join(map(str, series))}>")
