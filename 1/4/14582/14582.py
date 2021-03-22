score_table = [[], [], ]
flag = False
team_a = 0
team_b = 0

for i in range(0, 2):
    score_table[i] = input().split()

for i in range(0, 9):
    for j in range(0, 2):
        if j:
            team_b += int(score_table[j][i])
        else:
            team_a += int(score_table[j][i])
        if team_a > team_b:
            flag = True

if flag:
    print("Yes")
else:
    print("No")
