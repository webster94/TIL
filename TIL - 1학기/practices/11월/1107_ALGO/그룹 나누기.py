import sys
sys.stdin = open('그룹 나누기.txt','r')

def bfs(n):
    q = []
    q.append(n)
    visited[n] = 1
    while q:
        v = q.pop(0)
        for k in adj[v]:
            if not visited[k]:
                q.append(k)
                visited[k] = 1

T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    visited = [0] * (N+1)
    adj = [[] for _ in range(N+1)]
    cnt = 0
    for i in range(0,len(arr),2): # 왜 여기가 문제였누ㅜㅜ우우우
        adj[arr[i]].append(arr[i+1])
        adj[arr[i+1]].append(arr[i])
    for i in range(1,N+1):
        if not visited[i]:
            bfs(i)
            cnt +=1
    print('#{} {}'.format(t,cnt))
