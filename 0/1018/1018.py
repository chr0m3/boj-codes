def count_minimal_differences(table: list, x_offset: int, y_offset: int):
    global BLACK_START_TABLE
    global WHITE_START_TABLE

    black_count = 0
    white_count = 0
    for i in range(8):
        for j in range(8):
            if table[y_offset + i][x_offset + j] != BLACK_START_TABLE[i][j]:
                black_count += 1
            if table[y_offset + i][x_offset + j] != WHITE_START_TABLE[i][j]:
                white_count += 1

    return min(black_count, white_count)


BLACK_START_TABLE = [['B' for i in range(8)] for j in range(8)]
WHITE_START_TABLE = [['W' for i in range(8)] for j in range(8)]

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 1:
            BLACK_START_TABLE[i][j] = 'W'
            WHITE_START_TABLE[i][j] = 'B'

n, m = map(int, input().split())

input_table = list()
for i in range(n):
    input_table.append([c for c in input()])

minimal = 8 * 8

for i in range(n - 7):
    for j in range(m - 7):
        count = count_minimal_differences(input_table, j, i)

        if count < minimal:
            minimal = count

print(minimal)
