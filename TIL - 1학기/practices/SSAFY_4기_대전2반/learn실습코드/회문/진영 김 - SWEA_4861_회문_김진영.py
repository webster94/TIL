import sys

sys.stdin = open("input.txt", "r")

T = int(input())    # 3흡수기
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []

    for i in range(N):
        arr.append(list(input()))

    for i in range(N):      # 인풋 한줄을 검사하고 줄내려주는 반복문
        for j in range(N - M + 1):  # 기차가 칙칙폭폭폭
            rl = arr[i][j:j + M]
            ud = [arr[x][i] for x in range(j, j + M)]
            if rl == rl[::-1]:
                result = rl
            elif ud == ud[::-1]:
                result = ud

    print('#{}'.format(test_case), end=' ')
    rrsult = ''
    for i in result:
        rrsult += i
    print(rrsult)

