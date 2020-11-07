import sys, heapq
sys.stdin = open('최소이동거리.txt', 'r')

def bfs():
    dist = [0xffffff] * (N+1)
    visited = [False] * (N+1)
    q = []
    dist[0]=0
    q.append((dist[0],0))
    while q:
        w,v = q.pop(0)
        if not visited[v] :
            visited[v] = True
            for i in range(N+1):
                if not visited[i] and dist[i] > dist[v]+adj[v][i]:
                    dist[i] = dist[v]+adj[v][i]
                    q.append((dist[i],i))
    return dist[N]


T = int(input())
for t in range(1,T+1):
    N,E = map(int,input().split())
    adj = [[0xfffffff]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        st,en,w = map(int,input().split())
        adj[st][en] = w
    print(bfs())
