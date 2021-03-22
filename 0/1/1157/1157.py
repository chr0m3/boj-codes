string = input().upper()
character_count = list()

for i in range(0, 26):
    character_count.append(string.count(chr(i + 65)))

if character_count.count(max(character_count)) > 1:
    print('?')
else:
    print(chr(character_count.index(max(character_count)) + 65))
