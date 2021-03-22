a = 2
while a <= 100:
    b = 2
    while b <= a:
        c = b
        while c <= a:
            d = c
            while d <= a:
                if a * a * a == b * b * b + c * c * c + d * d * d:
                    print(f'Cube = {a}, Triple = ({b},{c},{d})')
                d += 1
            c += 1
        b += 1
    a += 1
