# 달팽이 방향정하고
# 입력받고
# 초기화하고
# 와일문으로 위치변경, 방향변경
# 출력

dr = [0,1,0,-1]
dc = [1,0,-1,0]
T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [ [0] * N for _ in range(N)]
    num = 1 # 시작값
    d= 0 # 방향전환 용
    r = 0 # 좌표용 행
    c = 0 # 좌표용 열
    while num < N*N:
        arr[r][c] = num
        num +=1
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            r,c = nr,nc # 바뀐 위치로 최신화
        else:# 아닐 경우 방향을 바꿔주자
            d = (d+1)%4
            r += dr[d]
            c += dc[d]
    print("#{}".format(t))
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end=' ')
        print()