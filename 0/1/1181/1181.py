words = [set() for i in range(51)]

for i in range(int(input())):
    word = input()
    words[len(word)].add(word)

for i in range(1, 51):
    for word in sorted(words[i]):
        print(word)
