def calc(h: int, w: int) -> int:
    global table

    if table[h][w] is not None:
        return table[h][w]

    table[h][w] = calc(h - 1, w) + calc(h, w - 1)
    return table[h][w]


table = [[None for j in range(15)] for i in range(15)]
for i in range(15):
    table[i][0] = 0
    table[0][i] = i

cases = int(input())
for i in range(cases):
    print(calc(int(input()), int(input())))
