a, b = map(lambda a: a[-1:-4:-1], input().split())

if int(a) > int(b):
    print(a)
else:
    print(b)
