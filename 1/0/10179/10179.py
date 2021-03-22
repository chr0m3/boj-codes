n = int(input())

for _ in range(n):
    price = float(input())
    discounted_price = round(price * 0.8, 2)
    print('${:.2f}'.format(discounted_price))
