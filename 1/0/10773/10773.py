import sys

input = sys.stdin.readline

k = int(input())

stack = list()
for _ in range(k):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))
