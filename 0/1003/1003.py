def fibonacci(n):
    global table
    if n in table.keys():
        return tuple(table[n])
    else:
        table[n] = (fibonacci(n - 1)[0] + fibonacci(n - 2)[0], fibonacci(n - 1)[1] + fibonacci(n - 2)[1])
        return tuple(table[n])


count_case = int(input())

for i in range(0, count_case):
    case = int(input())
    table = {0: (1, 0),
             1: (0, 1), }
    for j in range(2, case + 1):
        fibonacci(j)

    print('%d %d' % table[case])
