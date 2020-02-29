input()
numbers = dict()
for i in input().split():
    if i not in numbers:
        numbers[i] = 0
    numbers[i] += 1

input()
for i in input().split():
    if i in numbers:
        print(numbers[i], end=' ')
    else:
        print(0, end=' ')
