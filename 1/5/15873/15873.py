ab = input()

if ab[1] == '0':
    result = 10 + int(ab[2:])
else:
    result = int(ab[0]) + int(ab[1:])

print(result)
