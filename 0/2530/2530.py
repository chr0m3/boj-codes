a, b, c = map(int, input().split())
d = int(input())

estimate_sec = (c + d) % 60
estimate_min = (b + (c + d) // 60) % 60
estimate_hour = (a + ((b * 60 + c + d) // 3600)) % 24

print(f'{estimate_hour} {estimate_min} {estimate_sec}')
