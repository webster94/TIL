import sys, heapq

sys.stdin = open('최소이동거리.txt', 'r')


def diikstra():
    dist = [0xffffff] * (N + 1)
    visited = [False] * (N + 1)
    dist[0] = 0
    heap = []
    heapq.heappush(heap,(0,0))
    while heap:
        w,v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = True
            for i in range(1,N+1):
                if not visited[i] and dist[i] > dist[v] + adj[v][i]:
                    dist[i] = dist[v] + adj[v][i]
                    heapq.heappush(heap, (dist[i] ,i))
    return dist[N]


T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    adj = [[0xffffff] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        st, en, w = map(int, input().split())
        adj[st][en] = w
    print(diikstra())
