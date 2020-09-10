import sys
sys.stdin = open("정사각형의방.txt","r")
dr = [0,1,0,-1]
dc = [1,0,-1,0]

def BFS(a,b):
    q = []
    count = 1
    q.append((a,b))
    while q:
        curr_r,curr_c = q.pop(0)
        for k in range(4):
            nr = curr_r + dr[k]
            nc = curr_c + dc[k]
            if 0 <= nr < N and 0 <= nc <N and (arr[nr][nc]-arr[curr_r][curr_c]) == 1:
                count +=1
                q.append((nr,nc))
    return count

    #
    # for i in range(N):
    #     for j in range(N):
    #         if maxi < dist[i][j]:
    #             maxi = dist[i][j]

T= int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split()))for _ in range(N)]
    # 입력받음.

    # count == 이동한 방의 개수
    # 몇개의 방이동 ? BFS
    # BFS는 숫자가 1큰 값으로 이동시켜야한다
    # 이 때 이동횟수가 가장 큰 값을 저장하고 작은 숫자를 출력한다.
    # vistied _ list를 만들어야겠다.
    dist = [[0] * N for _ in range(N)]
    maxi = 0
    st = 0
    ans = []
    for i in range(N):
        for j in range(N):
            ans.append([arr[i][j], BFS(i,j)])
    ans.sort(key=lambda x: (-x[1], x[0]))
    print("#{} {} {}".format(t,ans[0][0], ans[0][1]))