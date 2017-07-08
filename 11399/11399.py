n = int(input())
time = list(map(int, input().split()))
time_sum = list()
sum = 0

for i in range(0, n):
    min_index = i
    for j in range(i, n):
        if time[min_index] > time[j]:
            min_index = j
    temp = time[i]
    time[i] = time[min_index]
    time[min_index] = temp

time_sum.append(time[0])

for i in range(1, n):
    time_sum.append(time_sum[i - 1] + time[i])

for i in range(0, n):
    sum += time_sum[i]

print(sum)
