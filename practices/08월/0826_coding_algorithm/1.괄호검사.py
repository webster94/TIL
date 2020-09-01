def check(bracket):
    #   인자로 넘어온 괄호들을 순회하면서 검사한다.
    #   여는 괄호라면 무조건 push
    #   닫는 괄호라면 일단 pop하고 스택에 top위치와 비교 제짝이면 continue
    #   제짝이 아니면 False
    #   끝까지 순회했을때 스택의 길이가 0이 아니라면 False
    stack = []

    for i in range(len(bracket)):
        if bracket[i] == '(' or bracket[i] == '{' or bracket[i] == '[':
            stack.append(bracket[i])
        elif bracket[i] == ')' or bracket[i] == '}' or bracket[i] == ']': # 닫힘괄호를 만나면
            if len(stack) == 0: # 빈 괄호면 false
                return False
            tmp = stack.pop()  #   있으면 맨 첫번째것을 제거?

            if bracket[i] == ')' and tmp == '(':
                continue
            elif bracket[i] == '}' and tmp == '{':
                continue
            elif bracket[i] == ']' and tmp == '[':
                continue

            return False
    if len(stack) > 0:
        return False

    return True


for _ in range(int(input())):
    bracket = input()

    print(check(bracket))