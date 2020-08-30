# 1.방향설정 젤 중요 ㅠㅠ
# 2. 입력을 받자
# 3. 빈배열 형성
# 4. 초기화
# 5. 출발!
# 6 벽을 만났을 경우 방향전환
# 7. 출력
# 우하좌상
dr = [0,1,0,-1]
dc = [1,0,-1,0]

T = int(input())
for t in range(1,T+1):
    N = int(input())
    # 입력 다 받았다.
    # 빈배열 만들자
    arr = [ [ 0 ] * N for _ in range(N)]
    # print(arr)
    # 초기화
    d = 0
    r = 0 # 실제 움직이는 좌표들임
    c = 0
    num = 1 # 시작까진 괜찮아
    while num <= N * N :
        arr[r][c] = num # 위치 최신화
        num +=1 #(다음 것대비)
        # 다음칸 대비를 못했네
        nr = r + dr[d] # 방향 따라 이동~
        nc = c + dc[d]  # 방향따라 이동!!

        if 0 <= nc < N  and 0 <= nr < N and arr[nr][nc] == 0:# 다음 경로 대비
             r,c = nr,nc  # 위치 변경
        else:
            d = (d + 1)%4  # 방향변경
            r += dr[d]
            c += dc[d]
    print("#",format(t))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()


