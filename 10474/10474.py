a, b = map(int, input().split())

while a != 0 and b != 0:
    c = int(a / b)
    a = a - c * b
    print("%d %d / %d" % (c, a, b))
    a, b = map(int, input().split())
