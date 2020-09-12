#괄호가 짝을 제대로 이루고 있는지 검사
#입력은 한줄의 파이썬 코드일 수 있고, 괄호만 주어질 수 있음
#정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력
#이거도 스택으로
#어제 한거니까 한번 내가 해보자!!!!
#짝을 이뤘는지 봐야되니까 일단 여는 괄호일때 스택에 넣기
#닫는 괄호일때 비교하고 같은 괄호유형이면 pop
#남은 stack이 있다면 짝을 이루지 못했으니 0, 없으면 1
import sys
sys.stdin = open('input.txt','r')
def check(code):
    top =''
    stack = []
    for i in range(len(code)):
        # print(code[i])
        if code[i] == '(' or code[i] == '{':
            stack.append(code[i])
            # print('{}을 추가했습니다'.format(stack))
        elif code[i] == ')' or code[i] == '}':
            if len(stack) == 0:
                return 0
            else:
                top = stack.pop()
                # print('{}을 제거했습니다'.format(stack))
            if code[i] == ')' and top == '(':
                continue
            elif code[i] == '}' and top == '{':
                continue
            return 0
    if len(stack) > 0:
        return 0
    return 1


T = int(input())
for tc in range(1,T+1):
    code = input()
    print('#{} {}'.format(tc,check(code)))