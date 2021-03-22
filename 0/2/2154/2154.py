import re

full_str = ''

for i in range(0, 100001):
    full_str += str(i)

print(re.search(input(), full_str).start())
