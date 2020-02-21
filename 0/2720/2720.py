test_cases = int(input())

for i in range(0, test_cases):
    money = int(input())
    quarter = int(money / 25)
    money %= 25
    dime = int(money / 10)
    money %= 10
    nickel = int(money / 5)
    penny = money % 5

    print('%d %d %d %d' % (quarter, dime, nickel, penny))
