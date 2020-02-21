students = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

for i in range(0, 28):
    students[int(input()) - 1] = 1

for i in range(0, 30):
    if students[i] == 0:
        print(i + 1)
