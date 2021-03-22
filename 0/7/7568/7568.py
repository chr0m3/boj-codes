import sys

input = sys.stdin.readline

n = int(input().rstrip())

arr = list()
for i in range(n):
    arr.append(tuple(map(int, input().rstrip().split())))

rank_list = list()
for i in range(n):
    rank = 1
    for j in range(n):
        if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
            rank += 1
    rank_list.append(str(rank))

print(' '.join(rank_list))
