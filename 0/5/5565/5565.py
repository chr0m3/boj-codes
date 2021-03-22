total_price = int(input())
price = list()

for i in range(0, 9):
    price.append(int(input()))

print(total_price - sum(price))
