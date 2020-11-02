import sys
sys.stdin = open('동철이의일분배.txt','r')
def P(s,percentage):
    global result
    if result >= percentage:
        return
    if s ==N:
        if result < percentage:
            result = percentage
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            P(s+1,percentage * arr[s][i])
            visited[i] = 0




T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] / 100
    visited = [0] * N
    result = 0
    P(0,1)
    print('#{} {}'.format(t,format(result*100,"7f")))
