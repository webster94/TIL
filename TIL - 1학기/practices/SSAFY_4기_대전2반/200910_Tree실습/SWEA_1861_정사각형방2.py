dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    dist = [1] * (N * N + 1)  # 거리
    num = [0] * (N * N + 1)  # 좌표

    # 방 입력
    arr = []

    for i in range(N):
        arr.append(list(map(int, input().split())))
        for j in range(N):
            # 해당 방 인덱스에 좌표 넣기
            num[arr[i][j]] = (i, j)

    # 2번부터 끝번호까지 수행
    for i in range(2, N * N + 1):
        for d in range(4):
            # 다음좌표확인
            # num[i][0] = 행, [1] = 열
            nr = num[i][0] + dr[d]
            nc = num[i][1] + dc[d]
            # 범위안에 들어오면서, 다음자리가 현재내 방번호보다 하나 작다면
            if 0 <= nr < N and 0 <= nc < N and i - 1 == arr[nr][nc]:
                # 현재방은 전방+1 거리만큼 이동가능
                dist[i] = dist[i - 1] + 1
                break

    ans_num, ans_dist = N * N, 0
    for i in range(1, N * N + 1):
        if dist[i] > ans_dist:
            ans_num = i
            ans_dist = dist[i]

    print("#{} {} {}".format(tc, ans_num - (ans_dist - 1), ans_dist))
