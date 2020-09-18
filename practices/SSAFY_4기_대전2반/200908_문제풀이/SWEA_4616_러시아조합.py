def combination(sel, idx, cnt):
    global ans

    if cnt == 2:
        print(sel)
        #각각의 1이 경계를 의미하고
        w = -1
        b = -1

        for i in range(N):
            if sel[i] == 1:
                if w == -1:
                    w = i
                else:
                    b = i

        count = 0

        #흰색 영역 칠하기
        for W  in range(0, w+1):
            for k in range(M):
                if flag[W][k] != 'W':
                    count +=1

        for B in range(w+1, b+1):
            for k in range(M):
                if flag[B][k] != 'B':
                    count+=1

        for R in range(b+1, N):
            for k in range(M):
                if flag[R][k] != 'R':
                    count +=1

        if count < ans:
            ans = count
        return

    if idx >= N-1:
        return

    #경계 뽑고
    sel[idx] = 1
    combination(sel, idx+1, cnt+1)
    #경계 다시 원상복구
    sel[idx] = 0
    combination(sel, idx+1, cnt)



T = int(input())

for tc in range(1, T+1):
    N , M = map(int, input().split())
    flag = [input() for _ in range(N)]

    ans = M*N

    combination([0]*N, 0, 0)

    print("#{} {}".format(tc, ans))