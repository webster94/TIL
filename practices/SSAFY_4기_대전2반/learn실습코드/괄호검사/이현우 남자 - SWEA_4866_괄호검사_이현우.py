def check(bracket):
    stack = []
    for i in range(len(bracket)):
        if bracket[i] == '(' or bracket[i] == '{' or bracket[i] == '[':
            stack.append(bracket[i])
        elif bracket[i] == ')' or bracket[i] == '}' or bracket[i] == ']':
            if len(stack) == 0:
                return 0
            tmp = stack.pop()

            if bracket[i] ==')' and tmp == '(':
                continue
            elif bracket[i] ==']' and tmp == '[':
                continue
            elif bracket[i] == '}' and tmp == '{':
                continue
            return 0
    if len(stack) > 0:
        return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    bracket = input()
    print('#{} {}'.format(tc,check(bracket)))