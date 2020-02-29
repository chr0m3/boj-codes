b, a = sorted(map(int, input().split()))

ta = a
tb = b
r = 1
while True:
    r = ta % tb
    if r == 0:
        break
    ta = tb
    tb = r

gcd = tb
lcm = int(a * b / gcd)

print(gcd)
print(lcm)
