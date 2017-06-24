room = int(input())
people = list(input().split())
a, b = map(int, input().split())

sum = 0

for i in people:
    if int(i) - a <= 0:
        sum += 1
        continue
    else:
        sum += 1
        if (int(i) - a) % b:
            sum += int((int(i) - a) / b) + 1
        else:
            sum += int((int(i) - a) / b)

print(sum)
