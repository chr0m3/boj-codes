numbers = list()

for i in range(0, 7):
    input_num = int(input())
    if input_num % 2 == 1:
        numbers.append(input_num)

if len(numbers) == 0:
    print('-1')
else:
    print(sum(numbers))
    print(min(numbers))
