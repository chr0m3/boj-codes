def decrypt(key):
    global crypto_num
    text = ''
    for num in crypto_num:
        text += charset[(num + key) % 26]
    return text


def check(text):
    global dictionary
    for word in dictionary:
        if word in text:
            return True
    return False


charset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]
crypto_text = input()
crypto_num = list()
dictionary_count = int(input())
dictionary = list()

for i in range(0, dictionary_count):
    dictionary.append(input())

for i in crypto_text:
    crypto_num.append(ord(i) - 97)

for i in range(0, 26):
    decrypt_text = decrypt(i)
    if check(decrypt_text):
        print(decrypt_text)
