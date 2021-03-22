def is_prime(n: int) -> bool:
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    m = int(input())
    n = int(input())

    prime_sum = 0
    prime_min = None
    for i in range(m, n + 1):
        if is_prime(i) is True:
            if prime_min is None:
                prime_min = i
            prime_sum += i

    print(f'{prime_sum}\n{prime_min}' if prime_sum > 0 else -1)
