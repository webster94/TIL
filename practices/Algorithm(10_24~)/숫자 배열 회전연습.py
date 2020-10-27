import sys
sys.stdin = open('숫자배열회전.txt','r')


def rotate(d):
    arr_new = [[0] * N for _ in range(N)]
    if d % 4 == 1:
        for i in range(N):
            for j in range(N):
                arr_new[j][N - i - 1] = arr[i][j]
        print(arr_new)
    elif d % 4 == 2:
        for i in range(N):
            for j in range(N):
                arr_new[N - i - 1][N - j - 1] = arr[i][j]
        print(arr_new)
    elif d % 4 == 3:
        for i in range(N):
            for j in range(N):
                arr_new[N - 1 - j][i] = arr[i][j]
        print(arr_new)
    else:
        for i in range(N):
            for j in range(N):
                arr_new[i][j] = arr[i][j]
        print(arr_new)
T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr =[list(map(int,input().split())) for _ in range(N)]
    d = 0
    arr_new = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i>=1 and j>=1:
                arr_new[j][N-i] = arr[i][j]
            else:
                arr_new[i][j] = arr[i][j]
    for i in range(N):
        print(arr_new[i])


