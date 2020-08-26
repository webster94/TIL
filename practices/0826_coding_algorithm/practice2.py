## 괄호 검색기
def check(arr):
    for i in range(len(arr)):
        if arr[i] == '(' : # push실시 push는 append~
            stack.append(arr[i])
        elif arr[i] == ')': # pop하고 비교 , 이때 비엇나 확인하기!!
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if stack  : return False  # 괄호에 남아있으면 False! 그렇지않으면 TRUE
    else: return True




stack = []
arr = "()()((()))"
print(check(arr))

