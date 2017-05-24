def calc(i):
    if i == 0:
        return 1
    else:
        return calc(i-2) * calc(n-(i-2))

n = int(input())
calc(n)
