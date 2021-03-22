vote = list()

for i in range(0, int(input())):
    vote.append(input())

if vote.count('0') > vote.count('1'):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')
