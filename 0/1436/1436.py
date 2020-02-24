count = int(input())

title = 0
while True:
    title += 1
    if '666' in str(title):
        count -= 1

    if count <= 0:
        break

print(title)
