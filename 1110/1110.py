n = int(input())
count = 1
m = (n % 10) * 10 + (n // 10 + n % 10) % 10

while n != m:
    count += 1
    m = (m % 10) * 10 + (m // 10 + m % 10) % 10

print(count)
