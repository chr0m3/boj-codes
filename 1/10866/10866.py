from collections import deque
import sys

input = sys.stdin.readline

count = int(input())
d = deque()

for i in range(0, count):
    command = input().split()
    if command[0] == 'push_front':
        d.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        d.append(int(command[1]))
    elif command[0] == 'pop_front':
        if len(d):
            print(d.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if len(d):
            print(d.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(d))
    elif command[0] == 'empty':
        if len(d):
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if len(d):
            print(d[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(d):
            print(d[len(d) - 1])
        else:
            print(-1)
