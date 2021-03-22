br, bc = map(int, input().split())
dr, dc = map(int, input().split())
jr, jc = map(int, input().split())

bessie = max(abs(br - jr), abs(bc - jc))
daisy = abs(dr - jr) + abs(dc - jc)

if bessie == daisy:
    print('tie')
elif bessie < daisy:
    print('bessie')
else:
    print('daisy')
