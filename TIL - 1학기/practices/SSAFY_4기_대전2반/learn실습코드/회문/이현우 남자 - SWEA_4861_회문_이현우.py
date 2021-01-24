T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            row = ''
            col = ''
            for k in range(M):
                row += arr[i][j+k]
                col += arr[j+k][i]
            if row == row[::-1]:
                print('#{} {}'.format(tc, row))
            if col == col[::-1]:
                print('#{} {}'.format(tc, col))