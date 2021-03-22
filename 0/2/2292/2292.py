n = int(input()) - 1

k = 0
while True:
    if n <= 3 * k * (k + 1):
        print(k + 1)
        break
    k += 1
