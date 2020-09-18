priority = {"*" : 2, "/" : 2, "+" : 1, "-" : 1, "(" : 0}
for t in range(1,11):
    input()
    line = input()
    ans = " "
    #스택준비
    stack = []

    for i in range(len(line)):
        # 괄호라면
        if line[i] == "(" or line[i] == ")":
            if line[i] == "(":
                stack.append(line[i])
            else:
                while stack[-1] != "(":
                    ans += stack.pop()
                # 여는 괄호 버리기
                stack.pop()
        elif line[i].isdigit(): # 읽고 있는게 숫자라면 바로 붙여넣어라
            ans += line[i]
        # 연산자 일때
        else:
            if len(stack) == 0:
                stack.append(line[i])
            else:
                # 연산자 우선순위를 비교해서
                # 스택에 탑에 있는 연산자가 현재 토큰의 우선순위보다 높거나 같다면
                while priority[stack[-1]] >= priority[line[i]]:
                    ans += stack.pop()
                    if len(stack) == 0:
                        break
                stack.append(line[i])

    while len(stack) > 0:
        ans += stack.pop()
    # 중위 표현식을 후위표현식으로 나타낸 표현임.

    for i in ans:

        # 숫자면 스택에 쌓기
        if i.isdigit():
            stack.append(int(i))
        #연산자이면 꺼내서 연산 후 다시 삽입
        else:
            B = stack.pop()
            A = stack.pop()
            if i == "+":
                stack.append(A+B)
            elif i == "-":
                stack.append(A-B)
            elif i == "*":
                stack.append(A*B)
            elif i == "/":
                stack.append(A/B)
    print("#{} {}".format(t,stack.pop()))