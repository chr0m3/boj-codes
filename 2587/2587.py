numbers = list()

for i in range(0, 5):
    numbers.append(int(input()))
numbers.sort()

print(int(sum(numbers) / 5))
print(numbers[2])
