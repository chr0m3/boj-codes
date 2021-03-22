prime_numbers = [True for x in range(1001)]
prime_numbers[1] = False

for i in range(2, 1001):
    for j in range(2*i, 1001, i):
        prime_numbers[j] = False

input()

count = 0
for i in map(int, input().split()):
    if prime_numbers[i] is True:
        count += 1

print(count)
