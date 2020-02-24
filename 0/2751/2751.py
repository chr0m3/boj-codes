import sys

counter = dict()

numbers = int(sys.stdin.readline().rstrip())
for i in range(numbers):
    number = sys.stdin.readline().rstrip()

    if number not in counter:
        counter[number] = 1
    else:
        counter[number] += 1

for i in range(-1000000, 1000001):
    if str(i) in counter:
        for _ in range(counter[str(i)]):
            print(i)
