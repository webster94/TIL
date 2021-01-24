import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    txt = input()
    stack = []
    ans = 0
    for char in txt:
        if char in '({':
            stack.append(char)
        elif char in '})':
            if len(stack)==0:
                break

            elif char == ')':
                if stack.pop() != '(':
                    break

            elif char == '}':
                if stack.pop() != '{':
                    break
    else:
        if len(stack)==0:ans = 1
    print('#{} {}'.format(t,ans))