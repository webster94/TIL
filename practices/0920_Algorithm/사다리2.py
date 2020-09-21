import sys
sys.stdin = open("사다리2.txt","r")
dr = [1,0,0]
dc = [0,1,-1]
def DFS(a,b):
    visited[a][b] = 1
    visit.append((a,b))
    if a == 99:
        return visit
    global count
    for k in range(3):
        nr = a + dr[k]
        nc = b + dc[k]
        count +=1
        print(count)
        if 0 <= nr < 100 and 0<= nc < 100 and visited[nr][nc] == 0 and arr[nr][nc] == 1:
            a,b = nr,nc







for t in range(1,11):
    arr = [list(map(int,input().split())) for _ in range(100)]
    count = 0
    result = []
    st,en = -1,-1
    for i in range(100):
        if arr[0][i] == 1:
            st,en = 0,i
            result.append([en,DFS(st,en)])
