def combination(a: int, b: int) -> int:
    """
    Choose b from a. a >= b
    """
    b = min(b, a - b)

    numerator = 1
    dominator = 1
    for i in range(b):
        numerator *= (a - i)
        dominator *= (b - i)

    return int(numerator / dominator)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        print(combination(m, n))
