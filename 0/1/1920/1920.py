import sys

input = sys.stdin.readline

input()
numbers = dict()
for i in input().split():
    numbers[i] = True

input()
for i in input().split():
    if i in numbers:
        print(1)
    else:
        print(0)
