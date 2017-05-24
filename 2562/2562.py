numbers = list()

for i in range(0, 9):
    numbers.append(int(input()))

temp_max = 0
temp_num = 0

for i in range(0, 9):
    if numbers[i] > temp_max:
        temp_max = numbers[i]
        temp_num = i

print(temp_max)
print(temp_num + 1)
