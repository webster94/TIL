import sys

sys.stdin = open('최소이동거리.txt', 'r')
import heapq


def diikstra():
    dist = [0xfffffff] * (V + 1)  # 거리 계산? 최대한 크게 저장해놓는다.
    visited = [0] * (V + 1)  # 방문체크 아직 미방문 !
    dist[0] = 0  # 시작할 곳 0
    heap = []  # heap을 사용하자
    heapq.heappush(heap, (0, 0))  # # 첫번째 인자는 원소를 추가할 대상 리스트, 두번째 인자는 추가할 원소를 넘깁니다,.
    while heap:
        w, v = heapq.heappop(heap)  # 가장 작은 heap에서 w,와 위치를 꺼낸다.
        if not visited[v]:  #
            visited[v] = 1
            dist[v] = w
            for i in range(1, V + 1):
                if not visited[i] and (dist[i] > dist[v] + adj[v][i]):
                    heapq.heappush(heap, (dist[v] + adj[v][i], i))
    return dist[V]


T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[0xffffff] * (V + 1) for _ in range(V + 1)]  # 가중치를 저장할 곳 최대한 크게 저장해놓는다.
    for i in range(E):
        st, ed, w = map(int, input().split())
        adj[st][ed] = w  # 유향, 가중치를 저장해놓는다.
    print(diikstra())
