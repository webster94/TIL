def check(line):
    for char in line:
        if char in '{(':
            stack.append(char)
        elif char in '})':
            if len(stack) == 0:
                return 0

            tmp = stack.pop()
            if char == '}' and tmp != '{':
                return 0
            elif char == ')' and tmp != '(':
                return 0
    if len(stack) > 0:
        return 0
    else:
        return 1

for tc in range(1, int(input())+1):
    text = input()
    stack = []
    print('#{} {}'.format(tc, check(text)))