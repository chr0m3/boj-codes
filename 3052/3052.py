numbers = list()
for i in range(0, 10):
    numbers.append(int(input()))

remainders = set([x % 42 for x in numbers])

print(len(remainders))
