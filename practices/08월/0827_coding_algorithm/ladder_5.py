# 입력을 받는다 리스트로 2차원배열!
# 출발지점을 찾는다!
# 좌,우 ,위 방향으로 이동시킨다!
# 도착지점을 찾에서 재귀 종료시킨다!
import sys
sys.stdin = open("input (31).txt", "r")


dr = [0,0,-1]
dc = [-1,1,0]
def DFS(a,b):
    arr[a][b] = 0
    if a ==0:
        return b
    for i in range(3):
        nr = a + dr[i]
        nc = b + dc[i]
        if nr<0 or nc <0 or nr >= 100 or nc >= 100:
            continue
        if arr[nr][nc] != 1:
            continue
        return DFS(nr,nc)


for tc in range(1,11):
    N = input()
    arr = [list(map(int,input().split())) for _ in range(100)]
    for i in range(100):
        st,en = -1,-1
        if arr[99][i] == 2:
            st,en = 99,i
            print("#{} {}".format(tc,DFS(st,en)))
