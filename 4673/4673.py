def d(n: int):
    result = n
    for i in str(n):
        result += int(i)
    return result


table = [True for i in range(10001)]

for i in range(1, 10001):
    result = d(i)
    if 1 <= result <= 10000:
        table[d(i)] = False

for i in range(1, 10001):
    if table[i]:
        print(i)
