sum = 0

for i in range(0, 5):
    temp = int(input())
    if temp < 40:
        sum += 40
    else:
        sum += temp

print('%d' % (sum / 5))
