n, m, k = map(int, input().split())

seat_n = int(k / m)
seat_m = k % m
print('%d %d' % (seat_n, seat_m))
