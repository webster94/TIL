import sys

sys.stdin = open('4886.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    sentence = input()
    stack = []
    res = 1
    for i in sentence:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')' or i == '}':
            if len(stack) == 0:
                res = 0
                break
            else:
                tmp = stack.pop()

                if i == '}' and tmp == '(':
                    res = 0
                    break
                elif i == ')' and tmp == '{':
                    res = 0
                    break



    if len(stack) > 0:
        res = 0

    print('#{} {}'.format(tc, res))
