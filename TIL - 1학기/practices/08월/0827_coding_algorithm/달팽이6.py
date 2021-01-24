# 방향 정하고
# 입력받고
# 빈배열 만들고
# 시작값 초기화
# 다음변수값 조정
# 와일문에서 방향전환과 현재위치 최신화
# 출력!

dr = [0,1,0,-1]
dc = [1,0,-1,0]
# 방향잡아써
# 입력받자
N = int(input())
# 빈배열
arr =  [[0]*N for _ in range(N)]
d = 0
r = 0
c = 0
num = 1
while num < N*N:
    arr[r][c] = num
    num +=1
    nr = r + dr[d]
    nc = c + dc[d]
    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] ==0 :
        r,c = nr,nc
    else:
        d = (d+1)%4
        r += dr[d]
        c += dc[d]

for i in range(N):
    for j in range(N):
        print(arr[i][j], end = ' ')


