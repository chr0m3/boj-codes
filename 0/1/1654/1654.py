import sys

input = sys.stdin.readline

k, n = map(int, input().split())

cables = list()
for _ in range(k):
    cables.append(int(input()))

left = 1
right = int(sum(cables) / n)
max_length = 0
while True:
    length = int((left + right) / 2)

    if left == right:
        if sum(map(lambda x: x // length, cables)) >= n:
            max_length = length
        print(max_length)
        break
    else:
        if sum(map(lambda x: x // length, cables)) >= n:
            # Search right side.
            max_length = length
            left = length + 1
        else:
            # Search left side.
            right = length - 1
