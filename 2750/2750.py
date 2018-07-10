n = int(input())
numbers = list()

for i in range(0, n):
    numbers.append(int(input()))
numbers.sort()

for i in numbers:
    print(i)
