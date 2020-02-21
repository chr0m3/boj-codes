import sys

fast_input = sys.stdin.readline

n = int(fast_input().rstrip())

for i in range(0, n):
    print(sum(map(int, fast_input().rstrip().split())))
