target = int(input())
now = 0

for i in range(0, target // 5 + 1):
    count_5k = target // 5 - i
    count_3k = 0
    if count_5k * 5 == target:
        print(count_5k + count_3k)
        break
    else:
        if (target - count_5k * 5) % 3 == 0:
            count_3k = (target - count_5k * 5) // 3
            print(count_5k + count_3k)
            break
        else:
            if count_5k == 0:
                print(-1)
