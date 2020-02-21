case_count = int(input())

for i in range(0, case_count):
    a, b = map(int, input().split())
    print('Case #%d: %d' % (i + 1, a + b))
