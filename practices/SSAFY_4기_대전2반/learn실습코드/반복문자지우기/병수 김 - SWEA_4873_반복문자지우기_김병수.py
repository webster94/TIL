T = int(input())

for tc in range(1, T+1):
    arr = list(input())
    n = len(arr)
    stack = []
    for i in range(n):
        # stack 이 비었거나 스택이 마지막값이 arr 내값과 같지 않으면 stack 에저장
        if not stack or arr[i] != stack[-1]:
            stack.append(arr[i])
        # stack 에 값이있고 스택의 마지막값과 arr 의 값이 일치하면 stack 에서 제거
        elif stack and arr[i] == stack[-1]:
            stack.pop()
    print('#{} {}'.format(tc, len(stack)))