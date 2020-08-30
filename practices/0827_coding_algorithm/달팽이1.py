# 방향 설정
#우하좌상
dr = [-1,0,1,0]
dc = [0,1,0,-1] # 순서정의 함

T = int(input())
for t in range(1,T+1):
    N = int(input())
    # 입력받았으니 이제 빈배열을 만들자
    arr = [[0] * N for _ in range(N)]
    # print(arr)
    # 이제 출발해보자
    # 초기화
    num = 1
    c = 0
    r = 0
    d = 0 # 1: 좌, 2:하 , 3: 우, 4:상

    while  num <= N * N:
        arr[r][c] = num
        num +=1
        # 다음칸을 설정
        nr = r + dr[d]
        nc = c + dc[d]
        if (0 <= nc < N and 0 <= nr < N and arr[nr][nc] == 0) : # 다음칸을 보는거지
            c , r = nc , nr  # 현재 좌표 갱신
        else:
            d = (d+1)%4
            r = r + dr[d]
            c = c + dc[d]
    print("#{}".format(t))
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end = ' ')
        print()