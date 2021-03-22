import math

ld, rh, rw = map(int, input().split())

lh = math.floor(math.sqrt((ld ** 2) / ((rh ** 2) + (rw ** 2)) * (rh ** 2)))
lw = math.floor(math.sqrt((ld ** 2) / ((rh ** 2) + (rw ** 2)) * (rw ** 2)))

print(f'{lh} {lw}')
