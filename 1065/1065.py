def is_hansu(x: int) -> bool:
    l = tuple(map(int, str(x)))
    if len(l) == 1:
        return True
    d = l[1] - l[0]
    for i in range(2, len(l)):
        if d != (l[i] - l[i-1]):
            return False
    return True


n = int(input())
hansu_count = 0

for i in range(1, n + 1):
    if is_hansu(i) is True:
        hansu_count += 1

print(hansu_count)
