string = input()
character_count = list()

for i in range(0, 26):
    character_count.append(string.count(chr(i + 97)))

print(' '.join(list(map(str, character_count))))
