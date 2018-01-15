max = 0
current = 0

for i in range(0, 4):
    out, in_ = map(int, input().split())

    current -= out
    if current > max:
        max = current

    current += in_
    if current > max:
        max = current

print(max)
