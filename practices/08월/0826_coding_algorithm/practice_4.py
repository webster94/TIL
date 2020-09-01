def DFS(v):
    print(v, end=" ")
    # 방문체크
    visited[v] = 1
    for i in range(1, V + 1):
        # 현재 내 정점 v 와 연결되어 있는지확인
        if arr[v][i] == 1 and visited[i] == 0:
            DFS(i)


# 입력 먼저
V, E = map(int, input().split())
# 인접행렬 생성 준비
arr = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    st, ed = map(int, input().split())
    # 무향 그래프이기 때문에 서로 연결되있음을 표시
    arr[st][ed] = arr[ed][st] = 1

# 방문 배열 선언
visited = [0] * (V + 1)
DFS(1)

# 7 8
# 1 2
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
#  3 7