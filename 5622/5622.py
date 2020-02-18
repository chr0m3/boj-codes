dial = input()

secs = 0

for d in dial:
    if 'A' <= d <= 'C':
        secs += 3
    elif 'D' <= d <= 'F':
        secs += 4
    elif 'G' <= d <= 'I':
        secs += 5
    elif 'J' <= d <= 'L':
        secs += 6
    elif 'M' <= d <= 'O':
        secs += 7
    elif 'P' <= d <= 'S':
        secs += 8
    elif 'T' <= d <= 'V':
        secs += 9
    elif 'W' <= d <= 'Z':
        secs += 10

print(secs)
