dice = list(map(int, input().split()))

if dice[0] == dice[1] == dice[2]:
    print(dice[0] * 1000 + 10000)
elif dice[0] == dice[1] or dice[1] == dice[2]:
    print(dice[1] * 100 + 1000)
elif dice[2] == dice[0]:
    print(dice[0] * 100 + 1000)
else:
    print(max(dice) * 100)
