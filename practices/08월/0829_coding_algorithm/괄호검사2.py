T = int(input())
for t in range(1,T+1):
    words = input()
    result = 1
    stack = []
    for i in range(len(words)):
        if words[i] == "(" or words[i] == "{":
            stack.append(words[i])
        elif words[i] == ")" or words[i] == "}":
            if len(stack) == 0:
                result = 0
                break
            tmp = stack.pop()
            if words[i] == ")" and tmp == "(":
                continue
            elif words[i] == "}" and tmp == "{":
                continue
            result = 0
    print(stack)
    if len(stack) > 0 :
        result = 0

    print("#{} {}" .format(t,result) )


