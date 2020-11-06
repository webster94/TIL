import sys

sys.stdin = open('탈주범.txt', 'r')


def bfs(a, b, l):
    q = [(a, b, l)]
    visited[a][b] = 1
    while q:
        r, c, cnt = q.pop(0)
        for dr, dc in directions[arr[r][c]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 0 and not visited[nr][nc] and cnt < L:
                if (-dr,-dc ) in directions[arr[nr][nc]]:
                    visited[nr][nc] = 1
                    q.append((nr, nc, cnt + 1))


directions = {
    0: [(0, 0)],
    1: [(-1, 0), (0, 1), (1, 0), (0, -1)],
    2: [(1, 0), (-1, 0)],
    3: [(0, 1), (0, -1)],
    4: [(-1, 0), (0, 1)],
    5: [(0, 1), (1, 0)],
    6: [(0, -1), (1, 0)],
    7: [(0, -1), (-1, 0)],
}

T = int(input())
for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    bfs(R, C, 1)
    result = 0
    for i in range(N):
        result += sum(visited[i])
    print("#{} {}".format(t,result))
