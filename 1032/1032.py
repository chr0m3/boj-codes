files = int(input())
file_names = list()

for i in range(0, files):
    file_names.append(input())

for i in range(0, len(file_names[0])):
    char = file_names[0][i]
    for j in range(0, files - 1):
        if file_names[j][i] != file_names[j + 1][i]:
            char = '?'
    print(char, end='')
