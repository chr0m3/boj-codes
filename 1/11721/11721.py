a = input()

for i in range(0, len(a) // 10 + 1):
    print(a[i*10:(i+1)*10])
