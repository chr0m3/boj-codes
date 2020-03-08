m, n = map(int, input().split())

numbers = [True for _ in range(0, n + 1)]

numbers[0] = False
numbers[1] = False

for i in range(2, n // 2 + 1):
    for j in [i * x for x in range(2, n // i + 1)]:
        numbers[j] = False

for i in range(m, n + 1):
    if numbers[i] is True:
        print(i)
