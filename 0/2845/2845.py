l, p = map(int, input().split())
articles = map(int, input().split())

prediction = l * p

for a in articles:
    print(a - prediction, end=' ')
