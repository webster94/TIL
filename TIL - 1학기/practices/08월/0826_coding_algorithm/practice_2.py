def check(arr):
    for i in range(len(arr)):
        if arr[i] == '(' :
            stack.append(arr[i])
        elif arr[i] == ')':
            if len(arr) == 0:
                return 0
            else:
                stack.pop()
        if arr[i] == '{' :
            stack.append(arr[i])
        elif arr[i] == '}':
            if len(arr) == 0:
                return 0
            else:
                stack.pop()
        if arr[i] == '[' :
            stack.append(arr[i])
        elif arr[i] == ']':
            if len(arr) == 0:
                return 0
            else:
                stack.pop()
    if len(stack) :
        return 0
    else:
        return 1
# if bracket[i] == '(' or bracket[i] == '{' or bracket[i]== '[':



stack = []
arr ="{()}{[]}"
arr1 = "([)](())"
arr2 = "(][())"
print(check(arr))
print(check(arr1))
print(check(arr2))