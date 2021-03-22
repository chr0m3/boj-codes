test_cases = int(input())

for i in range(0, test_cases):
    quiz_result = input()

    streak = 0
    score = 0

    for char in quiz_result:
        if char == 'O':
            streak += 1
            score += streak
        else:
            streak = 0

    print(score)
