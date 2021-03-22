import re


def check_is_group_word(s: str):
    for c in range(ord('a'), ord('z') + 1):
        re.compile(chr(c) + '+')
        if len(re.findall(re.compile(chr(c) + '+'), s)) >= 2:
            return False
    return True


group_word_num = 0
n = int(input())

for i in range(0, n):
    if check_is_group_word(str(input())) is True:
        group_word_num += 1

print(group_word_num)
