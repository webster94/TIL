import sys
import heapq

sys.stdin = open('최소이동거리.txt', 'r')


def dijstra():
    dist = [987654321] * (V + 1)
    visited = [False] * (V + 1)
    heap = []
    heapq.heappush(heap, (0, 0))
    dist[0] = 0

    while heap:
        w, v = heapq.heappop(heap)

        if not visited[v]:
            visited[v] = True
            dist[v] = w
            for i in range(V + 1):
                if not visited[i] and (dist[i] > dist[v] + adj[v][i]):
                    heapq.heappush(heap, (dist[v] + adj[v][i], i))  # 최솟값 색출
    return dist[V]  # V 자리까지 가는 법


T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[987654321] * (V + 1) for _ in range(V + 1)]  # 왜 큰 값을?설정
    for i in range(E):
        st, ed, w = map(int, input().split())
        adj[st][ed] = w
    # print(adj)
    print("#{} {}".format(t, dijstra()))
