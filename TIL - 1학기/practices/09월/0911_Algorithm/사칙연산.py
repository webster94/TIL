for tc in range(1,11):
    N = int(input())
    T = [[]] # 문자열로 여기다가 넣은 것이다.
    for i in range(1,N+1): # T[i]를 쓰기위해
        T.append(list(input().split())) # 첫번째 자료를 보고 해당하는 자리에 저장?
        if len(T[i]) == 4: # 연산자
            T[i][2] = int(T[i][2])
            T[i][3] = int(T[i][3])
        else:# 피연산자
            T[i][1] = int(T[i][1])

    def calc(v):
        if len(T[v]) ==2: # 피연산자,단말모드
            return T[v][1]

        else: # 연산자
            l = calc(T[v][2])
            r = calc(T[v][3])

            if T[v][1] == '+':return l+r
            elif T[v][1] == '-': return l-r
            elif T[v][1] == '*': return l*r
            else: return l/r



    print(calc(1))


