n = int(input())
score_list = list(map(int, input().split()))

m = max(score_list)
sum = 0

for i in range(0, n):
    sum += score_list[i] / m * 100

print('%.2f' % round(sum / n, 2))