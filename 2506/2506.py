streak = 0
score = 0

input()

results = input().split()

for result in results:
    if result == '1':
        streak += 1
        score += streak
    else:
        streak = 0

print(score)
