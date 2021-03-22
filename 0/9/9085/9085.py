test_cases = int(input())

for i in range(0, test_cases):
    number = int(input())
    numbers = input().split()
    sum_ = 0
    for j in range(0, number):
        sum_ += int(numbers[j])
    print(sum_)
