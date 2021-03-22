n, k = map(int, input().split())

combination = 1

for i in range(0, k):
    combination *= n - i
    combination /= i + 1

print(int(combination))
