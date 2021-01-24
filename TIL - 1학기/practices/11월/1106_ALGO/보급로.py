import sys
from collections import deque
import heapq
sys.stdin = open('보급로.txt', 'r')


def dijkstra():
    heap = []
    D[0][0] = 0
    heapq.heappush(heap,(D[0][0],0,0))

    while heap:
        w,y,x  = heapq.heappop(heap)
        # if D[x][y] >= D[N - 1][N - 1]: return
        for k in range(4):
            nr = y + dr[k]
            nc = x + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                tw = w + arr[nr][nc]
                if D[nr][nc] > tw:
                    D[nr][nc] = tw
                    heapq.heappush(heap, (D[nr][nc], nr, nc))
    return D[N-1][N-1]


dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    D = [[0xfffffff] * N for _ in range(N)]

    print("#{} {}".format(t, dijkstra()))
