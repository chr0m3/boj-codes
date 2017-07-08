score = list()
score_sum = [0, 0, 0, 0, 0]

for i in range(0, 5):
    score.append(list(map(int, input().split())))

for i in range(0, 5):
    for j in range(0, 4):
        score_sum[i] += score[i][j]

max_index = 0
for i in range(1, 5):
    if score_sum[i] > score_sum[max_index]:
        max_index = i

print("%d %d" % (max_index + 1, score_sum[max_index]))
