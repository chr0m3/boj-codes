from itertools import combinations

n, m = map(int, input().split())
cards = map(int, input().split())

total = 0
for i in combinations(cards, 3):
    temp = sum(i)

    if total < sum(i) <= m:
        total = temp
        if temp == m:
            break

print(total)
