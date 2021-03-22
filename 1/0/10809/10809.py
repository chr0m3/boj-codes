string = input()
character_offset = list()

for i in range(0, 26):
    character_offset.append(string.find(chr(i + 97)))

print(' '.join(list(map(str, character_offset))))
