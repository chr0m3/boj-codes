import sys

input = sys.stdin.readline

stack = list()

while True:
    balanced = True
    string = input()
    if string == '.\n':
        break

    for char in string:
        if char == '(':
            stack.append('(')
        elif char == '[':
            stack.append('[')
        elif char == ')':
            if len(stack) == 0 or stack.pop() != '(':
                balanced = False
        elif char == ']':
            if len(stack) == 0 or stack.pop() != '[':
                balanced = False

    if len(stack) != 0:
        balanced = False
        stack.clear()

    if balanced is True:
        print('yes')
    else:
        print('no')
