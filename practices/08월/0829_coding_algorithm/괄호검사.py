# 입력받고
# # check 함수를 만들어서 체크하자
#스택을 써야함
#continue를 사용해보자

T= int(input())
for t in range(1,T+1):
    words = input()
    stack = []
    result = 1
    for i in words:
        if i == '{' or i == '(' :
            stack.append(i)
        elif i == '}' or i == ')':
            if len(stack) == 0:
                result = 0
                break
            tmp = stack.pop()  # 제거 할때 비교를하기위해 if 사용
            if i == ')' and tmp == '(':  #
                continue
            elif i == '}' and tmp == '{':
                continue
            result = 0
    if len(stack) > 0:
        result = 0
    print("#{} {}".format(t,result))


