hour, min = map(int, input().split())
time = int(input())

estimate_hour = (hour + (time + min) // 60) % 24
estimate_min = (time + min) % 60

print(f'{estimate_hour} {estimate_min}')
