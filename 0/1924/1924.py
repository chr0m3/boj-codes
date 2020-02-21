def calc_days(x, y):
    days = 0
    days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, ]

    for i in range(1, x):
        days += days_month[i - 1]

    return days + y - 1


x, y = map(int, input().split())
date = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN', ]
print(date[calc_days(x, y) % 7])
