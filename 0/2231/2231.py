def find(n: int):
    for i in range(1, 1000001):
        total = 0
        for j in str(i):
            total += int(j)
        total += i
        if total == n:
            print(i)
            return
    print(0)


find(int(input()))
