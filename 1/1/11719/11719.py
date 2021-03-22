while True:
    try:
        str_ = str(input())
        print(str_)
    except EOFError:
        break
