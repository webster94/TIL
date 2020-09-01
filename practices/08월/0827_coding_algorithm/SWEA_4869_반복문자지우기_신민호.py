T = int(input())
for t in range(1,T+1):
    tc = input()
    stack = []

    for i in range(len(tc)):
        if len(stack) == 0 or tc[i] != stack[-1]:
            stack.append(tc[i])
        else:
            stack.pop()
    print("#{} {}".format(t,len(stack)))


## 교수님
for tc in range(1,int(input())+1):
    arr = input()
    S = []

    for ch in arr:
        if not S:
            S.append(ch) ## 빈스택인 경우
        elif ch != S[-1]:
            S.append(ch)
        else:
            S.pop()

    print(len(S))