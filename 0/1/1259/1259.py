while True:
    input_str = input()
    n = int(input_str)

    if n == 0:
        break

    m = int(input_str[::-1])

    if n == m:
        print('yes')
    else:
        print('no')
