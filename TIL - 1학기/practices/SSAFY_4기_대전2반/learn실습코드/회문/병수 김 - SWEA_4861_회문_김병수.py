import sys

sys.stdin = open('4861.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(input() for _ in range(N))
    res = []

    # 가로에서 회문 찾기
    for i in range(N):
        for j in range(N - M + 1):
            if arr[i][j:j + M] == arr[i][j:j + M][::-1]:
                res.append(arr[i][j:j + M])

    # 세로에서 회문 찾기

    for i in range(N- M + 1):
        for j in range(N):
            res2 = []
            for x in range(M):
                res2.append(arr[i+x][j])
            if res2 == res2[::-1]:
                res.append(''.join(res2))


    print('#{} {}'.format(tc, res[0]))
