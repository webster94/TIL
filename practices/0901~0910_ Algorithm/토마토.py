# # 토마토 문제 푸는 법.
# 1. 다 익었는 지 확인 하는 법은 1로 바꿀 때 카운트를 달아서 개수를 올라가게 하자
# 2. -1이 벽으로 하고
# 3. 처음에 q의 좌표를 담아서 시작하게 돌리자.
# 처음 와일문의 실행될때 날짜 카운트 하고 이동할때 카운트 돌리자
# 그리고 마지막에 이중포문으로 확인시키자 . 모두다 1이면 0  0이 있으면 -1!
#
# 좋아써
# 함수호출

dr = [0,1,0,-1]
dc = [1,0,-1,0]
def BFS(q):
    # 모두 1로 만들어버리는 bfs\
    global cnt_day
    cnt_to = 0
    size = len(q)
    while q:
        curr_r,curr_c = q.pop(0)
        cnt_day +=1 # 날짜를 의미
        # print(curr_r,curr_c)
        dist[curr_r][curr_c] = 1
        print(dist)
        while size:
            for a in range(4):
                nr = curr_r + dr[a]
                nc = curr_c + dc[a]
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and dist[nr][nc] == 0:
                    dist[nr][nc] = 1
                    cnt_to += 1
                    q.append((nr,nc))
            size -= 1
            print(dist)



import sys
sys.stdin = open("토마토.txt","r")
T = int(input())
for t in range(1,T+1):
    M,N = map(int,input().split()) # 가로,세로
    arr = [list(map(int,input().split())) for _ in range(N)]
    dist = [[0]*M for _ in range(N)]
    cnt_day = 0
    # 1을 먼저 확인하자/
    q = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i,j))
    BFS(q)


