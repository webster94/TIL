

T = int(input())

for tc in range(1, T+1):
    bracket = True
    arr = input()
    test_str = []

    for ch in arr:
        if ch == '{' or ch =='(' :
            test_str.append(ch)
        elif ch == ')' or ch == '}' :
            # 빈 스택일 경우
            if len(test_str) == 0:
                bracket = False
                break
            else:
                brackets = test_str.pop()
                if brackets == '(' and ch != ')' :
                    bracket = False
                    break
                elif brackets == '{' and ch != '}' :
                    bracket = False
                    break
    if bracket and len(test_str) == 0:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.formate(tc))