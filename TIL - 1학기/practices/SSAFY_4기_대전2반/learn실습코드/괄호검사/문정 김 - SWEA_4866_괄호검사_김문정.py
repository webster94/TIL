# testcase 10개 중 1개 fail, 예상되는 반례: ))(( 처럼 짝은 맞지만 닫힌 괄호가 먼저 온 경우.
# 정상: 1, 아니면 0
# stack에 여는 괄호 넣고, 닫는 괄호 나오면 
#   1. 닫는 괄호를 stack에 추가하고 
#   2. 닫는 괄호와(리스트의 원소) stack에서 꺼낸 값이 짝인지 확인
#   for문 다 돌았는데 stack이 비지 않았다면 False
def check(lis):
    for li in lis:
        if li == '(' or li == '{': # 여는 괄호이면 stack에 추가
            stack.append(li)
        elif li == ')' or li == '}': # 닫는 괄호나오면 리스트원소(li)와 stack에서 꺼낸 값이 짝인지 확인
            if len(stack) == 0: # stack에서 꺼내기 전에 빈 stack인지 확인
                return False
            tmp = stack.pop()
            if li == ')' and tmp == '(':
                continue
            if li == '}' and tmp == '{':
                continue
    if len(stack) > 0:
        return False
    return True

T = int(input())
for tc in range(1, T+1):
    stack = []
    texts = input()
    if check(texts):
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))
