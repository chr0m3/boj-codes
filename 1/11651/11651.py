from functools import cmp_to_key
import sys


def point_compare(a: tuple, b: tuple):
    if a[1] == b[1]:
        return a[0] - b[0]
    return a[1] - b[1]


input = sys.stdin.readline

n = int(input())

points = list()
for i in range(n):
    points.append(tuple(map(int, input().split())))

for p in sorted(points, key=cmp_to_key(point_compare)):
    print(f'{p[0]} {p[1]}')
