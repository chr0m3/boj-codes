count, target = map(int, input().split())
numbers = tuple(input().split())
str = ''

for i in numbers:
    if int(i) < target:
        str += i + ' '

print(str)