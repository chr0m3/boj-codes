target = int(input())
now = 0

for i in range(0, target // 5 + 1):
    if (target // 5 - i) * 5 == target:
        print("5kg")
        print(target // 5 - i)
        print("3kg")
        print(0)
        break
    else:
        now = (target // 5 - i) * 5
        while now < target:
            now += 3
            if now == target:
                print("5kg")
                print(target // 5 - i)
                print("3kg")
                print((now - ((target // 5 - i) * 5)) / 3)
                break
