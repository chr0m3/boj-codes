n = int(input())
line = list()
numbers = list(map(int, input().split()))

for i in range(0, n):
    line.insert(len(line) - numbers[i], i + 1)

print(" ".join(map(str, line)))
