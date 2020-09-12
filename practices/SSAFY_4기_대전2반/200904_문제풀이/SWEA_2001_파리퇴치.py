def flapper(r, c):
    total = 0

    #해당시작점부터 +M크기 만큼
    for i in range(r, r+M):
        for j in range(c, c+M):
            total += fly[i][j]

    return total

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    fly = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for i in range(N-M+1):
        for j in  range(N-M+1):
            #파리채로 때려잡는 이중 포문
            tmp = flapper(i,j)
            if ans <tmp:
                ans= tmp
            # ans = max(ans , tmp)

    print("#{} {}".format(tc, ans))