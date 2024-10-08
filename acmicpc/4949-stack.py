from collections import deque

result = []

def func(data):
    stack = []
    for i in data:
        if i == '[':
            stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return 'no'
            else:
                stack.pop()
        elif i == ']':
            if len(stack) == 0 or stack[-1] != '[':
                return 'no'
            else:
                stack.pop()
    return 'yes' if len(stack) == 0 else 'no'


while True:
    data = input()
    if data == '.':
        break
    else:
        result.append(func(data))

print('\n'.join(result))