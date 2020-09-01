def check():
    #전체 크기가 N
    for i in range(N):
        #가로 검사
        for j in range(N-M+1):
            tmp = words[i][j:j+M]
            if tmp == tmp[::-1]:
                return tmp
        #세로 검사
        for j in range(N-M+1):
            tmp = []
            for k in range(M):
                tmp.append(words[j+k][i])
            if tmp == tmp[::-1]:
                return tmp

    return []

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    words = [list(input()) for _ in range(N)]

    ans = check()

    print("#{} {}".format(tc, ''.join(ans)))
