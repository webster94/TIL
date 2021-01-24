def calc(A,op,B):
    if op == '+':
        return A+B
    elif op == '-':
        return A-B
    elif op == '*':
        return A*B
    elif op == '/':
        return A//B

    return 0

T = int(input())

for tc in range(1, T+1):
    line = input().split()
    stack = []

    flag = True
    #가장 마지막은 항상 . 으로 주어진다.
    for i in range(len(line)-1):
        if line[i].isdigit():
            stack.append((int(line[i])))
        else:
            if len(stack) < 2:
                flag = False
                break

            B = stack.pop()
            A = stack.pop()

            stack.append(calc(A,line[i],B))

    if flag and len(stack)==1:
        print("#{} {}".format(tc, stack.pop()))
    else:
        print("#{} {}".format(tc, "error"))
