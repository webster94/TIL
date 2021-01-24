priority = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

for tc in range(1, 11):
    input()
    line = input()
    ans = ''
    #스택 준비
    stack = []

    for i in range(len(line)):
        #괄호라면
        if line[i] == '(' or line[i] == ')':
            #여는 괄호는 우선순위가 제일 높으므로 무조건 삽입
            if line[i] == '(':
                stack.append(line[i])
            else:
                #여는괄호가 나올때까지 무조건 pop
                while stack[-1] != '(':
                    ans += stack.pop()
                #여는 괄호하나 버리기
                stack.pop()
        elif line[i].isdigit():
            ans += line[i]
        #연산자일때
        else:
            if len(stack)==0:
                stack.append(line[i])
            else:
                #연산자 우선순위를 비교해서
                #스택에 탑에 있는 연산자가 현재 토큰의 우선순위보다 높거나 같다면
                while priority[stack[-1]] >= priority[line[i]]:
                    ans += stack.pop()
                    if len(stack) == 0:
                        break
                stack.append(line[i])

    #남아있는 스택 비우기
    while len(stack) >0:
        ans += stack.pop()
###############################################중위 표현식 -> 후위표현식

    for i in ans:
        #숫자면 스택에 쌓기
        if i.isdigit():
            stack.append(int(i))
        #연산자이면 꺼내서 연산후 다시 삽입
        else:
            B = stack.pop()
            A = stack.pop()
            if i == '+':
                stack.append(A+B)
            elif i == '-':
                stack.append(A-B)
            elif i == '*':
                stack.append(A*B)
            elif i == '/':
                stack.append(A/B)

    print("#{} {}".format(tc, stack.pop()))
