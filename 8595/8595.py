import re

regex = re.compile('\d+')
input()
str_ = input()
list_ = regex.findall(str_)

sum = 0

for n in list_:
    sum += int(n)

print(sum)
