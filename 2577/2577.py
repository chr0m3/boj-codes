a = int(input())
b = int(input())
c = int(input())

mul = str(a * b * c)

for i in range(0, 10):
    count = 0
    for j in mul:
        if i == int(j):
            count += 1
    print(count)
