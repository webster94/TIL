dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def DFS(r, c, line):
    if len(line) == 7:
        # tmp = ''.join(line)
        # if tmp not in ans:
        #     ans.append(tmp)
        ans.add(line)
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nc < 0 or nr >= N or nc >= N:
            continue
        line += [arr[nr][nc]]
        # line.append(arr[nr][nc])
        # DFS(nr, nc, line)
        # line.pop()
        DFS(nr,nc, line+arr[nr][nc])
        # if 0<=nr<N and 0<=nc<N:
        #     DFS 코드


T = int(input())

for tc in range(1, T + 1):
    N = 4
    arr = [input().split() for _ in range(N)]
    # ans = []
    ans = set()

    for i in range(N):
        for j in range(N):
            # DFS(i, j, [arr[i][j]])
            DFS(i,j, arr[i][j])

    print("#{} {}".format(tc, len(ans)))
