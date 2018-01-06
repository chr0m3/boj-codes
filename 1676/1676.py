n = int(input())
factorial = 1
answer = 0

for i in range(1, n + 1):
    factorial *= i

for i in range(0, len(str(factorial))):
    if factorial % 10 != 0:
        print(answer)
        break
    else:
        factorial = int(str(factorial)[0:len(str(factorial)) - 1])
        answer += 1
