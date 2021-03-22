a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

a_price = a * p
if p <= c:
    b_price = b
else:
    b_price = b + (p - c) * d

print(min(a_price, b_price))
