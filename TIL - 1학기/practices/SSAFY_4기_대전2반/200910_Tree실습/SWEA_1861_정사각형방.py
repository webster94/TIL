dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def BFS(stR, stC):
    global ans_num, ans_dist
    queue = [(stR, stC)]
    cnt = 0

    while queue:
        r, c = queue.pop(0)
        #하나 꺼냈다는 것은 한칸 이동하는 거니까 +1
        cnt += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            #띠를 둘러놔서 범위쳌 필요없음, 다음좌표 - 현재좌표의 값이 1 이라면 이동가능!
            if arr[nr][nc] - arr[r][c] == 1:
                queue.append((nr,nc))

    #지금 cnt 가 구한 거리값보다 크다면
    if cnt >= ans_dist:
        if cnt == ans_dist:
            #같으면 시작점 더 작은값으로 갱신
            ans_num = min(ans_num, arr[stR][stC])
        else:
            #아니라면 그냥 갱신
            ans_num = arr[stR][stC]
        #요거 위치는 else 밑에 있어도 됨.. ㅎㅎ
        ans_dist = cnt


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    #띠를 두르는 작업 상하좌우 한칸씩 더크게 만들기
    arr = [[0] * (N + 2) for _ in range(N + 2)]

    #실제로 사용하는 곳은 1부터 N까지
    for i in range(1, N + 1):
        tmp = list(map(int, input().split()))
        #1부터 N까지
        for j in range(1, N + 1):
            #tmp는 한개 차이가나니 -1
            arr[i][j] = tmp[j - 1]

    ans_dist = 0#거리 담기
    ans_num = 0#시작 번호담기

    #모든 지점 다해보기
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            BFS(i, j)

    print("#{} {} {}".format(tc, ans_num, ans_dist))