import itertools

height = list()

for i in range(0, 9):
    height.append(int(input()))

height.sort()

for i in itertools.combinations(height, 7):
    if sum(i) == 100:
        for j in i:
            print(j)
