import sys
sys.stdin = open("input_delete.txt", "r")

def check(text):
    stack.append(text[0])
    for i in range(1, len(text)):
        if len(stack) != 0:
            if stack[-1] != text[i]:
                stack.append(text[i])
            else:
                stack.pop()
        else:
            stack.append(text[i])
    return len(stack)

for tc in range(1, int(input())+1):
    text = input()
    stack = []

    print('#{} {}'.format(tc, check(text)))