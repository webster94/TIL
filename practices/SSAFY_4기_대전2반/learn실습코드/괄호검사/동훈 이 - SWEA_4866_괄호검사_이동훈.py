def stack(arr):
    for i in arr:
        if i == "{" or i == "(":
            blank_list.append(i)
        elif i == "}" or i == ")":
            if len(blank_list) == 0:
                return 0
            tmp = blank_list.pop()

            if i == ")" and tmp == "(":
                continue
            elif i == "}" and tmp == "{":
                continue
            
            return 0
    if len(blank_list) > 0:
        return 0
    return 1
    


T = int(input())
for i in range(1, T+1):
    arr = list(input())

    blank_list = []
    print("#{} {}".format(i, stack(arr)))