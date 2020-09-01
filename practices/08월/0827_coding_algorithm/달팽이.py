#우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input()) # 입력받기

for tc in range(1, T+1):
    N = int(input())  #  N*N배열

    arr = [[0] * N for _ in range(N)]   # 0배열 선언

    d = 0 #방향 0 : 우 , 1 : 하, 2 : 좌 , 3 : 상   #방향
    r = 0 # 좌표들
    c = 0
    num = 1 # 시작점

    while num <= N * N:
        arr[r][c] = num #현재칸에 값을 저장장
        num += 1 # 다음 숫자 준비

        #다음칸을 결정
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<= nr <N and 0 <= nc <N and arr[nr][nc] == 0:  # 위에서 우로 바뀔때 중요하다.
            #현재좌표를 갱신
            r, c = nr , nc
        else:
            d = (d+1)%4  # 방향임
            r += dr[d]
            c += dc[d]

    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()