case_count = int(input())

for i in range(0, case_count):
    num, str = map(lambda a: a, input().split())
    return_str = ''
    for char in str:
        return_str += char * int(num)
    print(return_str)
