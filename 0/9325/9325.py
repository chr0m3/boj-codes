count_case = int(input())

for i in range(0, count_case):
    sum = int(input())
    n = int(input())

    for i in range(0, n):
        q, p = map(int, input().split())
        sum += q * p

    print(sum)
