import sys
sys.stdin = open('숨바꼭질.txt','r')
def dfs(n):
    q = []
    q.append(n)
    while q:
        x = q.pop(0)
        if x ==K:
            return visited[x]
        for nx in (x-1,x+1,2*x):
            if 0<=nx < 100001 and visited[nx]== 0:
                q.append(nx)
                visited[nx] = visited[x] + 1

N,K = map(int,input().split())
visited = [0] * 100001
# 갈 수 있는 곳을 모두 나타내서 정답이 나오면  몇번째 수 인지 리턴!
print(dfs(N))
