def calc_average(case):
    sum = 0
    count = int(case[0])
    for i in range(1, count + 1):
        sum += int(case[i])
    return sum / count


def count_average(case, average):
    count = 0
    count_num = int(case[0])
    for i in range(1, count_num + 1):
        if average < int(case[i]):
            count += 1
    return count


count_case = int(input())
cases = list()

for i in range(0, count_case):
    cases.append(list(input().split()))

for case in cases:
    average = calc_average(case)
    print('%.3f' % round(count_average(case, average) / int(case[0]) * 100, 3) + '%')
