import sys
sys.stdin = open('월말1번.txt','r')

def color(i,j):
    for a in range(i,N-i):
        for b in range(j,N-j):
            arr[a][b] =M + (N//2 -i) * D


T = int(input())
for t in range(1,T+1):
    N,M,D = map(int,input().split())
    arr = [[0] * N for _ in range(N)]
    for i in range(N//2):
        for j in range(N//2):
            if i==j:
                color(i,j)
    arr[N // 2][N // 2] = M
    for i in range(N):
        print(sum(arr[i]) ,end = ' ')
    print()
    # arr[i][j] = M + (N // 2 - i) * D