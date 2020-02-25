from collections import deque

count = int(input())
cards = deque([i for i in range(1, count + 1)])

if count == 1:
    print(1)
    exit(0)

while True:
    cards.popleft()
    count -= 1

    if count <= 1:
        print(cards.popleft())
        break

    cards.append(cards.popleft())
