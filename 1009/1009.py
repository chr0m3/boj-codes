case_count = int(input())
table = [
            [10, ],
            [1, ],
            [2, 4, 8, 6, ],
            [3, 9, 7, 1, ],
            [4, 6, ],
            [5, ],
            [6, ],
            [7, 9, 3, 1, ],
            [8, 4, 2, 6, ],
            [9, 1, ],
        ]

for i in range(0, case_count):
    a, b = map(int, input().split())
    print(table[a % 10][b % len(table[a % 10]) - 1])
