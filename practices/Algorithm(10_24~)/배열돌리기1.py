def rotate(arr,arr_new1,visited,cnt):
    if cnt == 0:
        return arr_new1
    arr_new2 = [[0] * M for _ in range(N)]
    for i in (0, N - 1):
        for j in (0, M - 1):
            if i == 0 and j == 0:
                while i < N - 1 and visited[i][j] == 0:
                    visited[i][j] = 1
                    arr_new1[i + 1][j] = arr[i][j]
                    i += 1
                while j < M - 1 and visited[i][j] == 0:
                    visited[i][j] = 1
                    arr_new1[i][j + 1] = arr[i][j]
                    j += 1
            elif i == N - 1 and j == M - 1:
                a = 0
                while i > 0 and visited[i][j] == 0:
                    visited[i][j] = 1
                    arr_new1[i - 1][j] = arr[i][j]
                    i -= 1
                while j > 0 and visited[i][j] == 0:
                    visited[i][j] = 1
                    arr_new1[i][j - 1] = arr[i][j]
                    j -= 1
    arr_new2 = arr_new1[::]
    return rotate(arr_new1,arr_new2,visited,cnt-1)


N,M,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
arr_new1 = [[0] * M for _ in range(N)]
cnt = 1
print(rotate(arr,arr_new1,visited,cnt))




