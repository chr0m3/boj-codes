from collections import deque
import sys

input = sys.stdin.readline

count = int(input())
queue = deque()

for i in range(0, count):
    command = input().split()
    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(queue):
            print(queue[len(queue) - 1])
        else:
            print(-1)
