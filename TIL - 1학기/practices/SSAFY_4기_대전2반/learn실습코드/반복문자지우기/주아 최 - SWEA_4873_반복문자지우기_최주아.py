import sys
sys.stdin = open("input2.txt","r")

def check(word):
    stack = []
    newList = list(word)
    for i in range(len(newList)):
        if len(stack) == 0:
            stack.append(newList[i])
        elif newList[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(newList[i])

    return len(stack)


for T in range(1, int(input()) + 1):
    word = input()
    print('#{} {}'.format(T, check(word)))
