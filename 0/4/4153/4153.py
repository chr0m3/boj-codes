while True:
    lengths = list(map(int, input().split()))
    lengths.sort()

    if lengths[2] == 0:
        break

    if lengths[0] ** 2 + lengths[1] ** 2 == lengths[2] ** 2:
        print('right')
    else:
        print('wrong')
