def is_vps(s: str):
    level = 0

    for j in s:
        if j == '(':
            level += 1
        else:
            level -= 1

        if level < 0:
            return False

    if level == 0:
        return True
    else:
        return False


n = int(input())

for i in range(0, n):
    input_str = input()
    if is_vps(input_str) is True:
        print('YES')
    else:
        print('NO')
