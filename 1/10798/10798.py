words = [[None for i in range(0, 15)] for i in range(0, 5)]

for i in range(0, 5):
    input_str = input()
    for j in range(0, len(input_str)):
        words[i][j] = input_str[j]

for i in range(0, 15):
    for j in range(0, 5):
        if words[j][i] is not None:
            print(words[j][i], end='')
