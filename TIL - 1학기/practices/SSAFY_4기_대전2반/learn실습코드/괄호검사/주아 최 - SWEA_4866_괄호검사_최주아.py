import sys
sys.stdin = open("input3.txt","r")


def check(word):
    stack = []
    checkList = ['[',']','{','}','(', ')']

    for i in range(len(word)):
        if word[i] not in checkList:
            continue

        elif word[i] == '(' or word[i] == '[' or word[i] == '{':
            stack.append(word[i])

        elif word[i] == ')' or word[i] == ']' or word[i] == '}':
            if len(stack) == 0:
                return 0

            if word[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif word[i] == ']' and stack[-1] == '[':
                stack.pop()
            elif word[i] == '}' and stack[-1] == '{':
                stack.pop()




    if len(stack) != 0:
        return 0
    return 1

for T in range(1, int(input()) + 1):
    word = input()
    print('#{} {}'.format(T, check(word)))