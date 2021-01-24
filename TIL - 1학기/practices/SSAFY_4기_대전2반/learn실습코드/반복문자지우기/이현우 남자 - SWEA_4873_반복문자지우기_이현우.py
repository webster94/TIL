def check(arr):
    stack = []
    for i in range(len(arr)):
        if len(stack):
            if arr[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(arr[i]) 
        else:
            stack.append(arr[i])
    return len(stack)
    
T = int(input())
for tc in range(1,T+1):
    arr = input()
    print('#{} {}'.format(tc, check(arr)))