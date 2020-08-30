import sys
import copy
sys.stdin = open("input (31).txt", "r")
# 입력을 받고
# 출발지점 찾아
# 앞으로 가는 dfs를 적자
# 도착지점!!
dr = [0,0,-1]
dc = [-1,1,0]
def DFS(i,j):
    arr[i][j] = 0
    if i == 0 :
        return j
    for k in range(3):
        nr = i + dr[k]
        nc = j + dc[k]
        print(nr,nc)
        if 0 <= nr < 100 and 0 <= nc < 100 and arr[nr][nc] ==1:
            return DFS(nr,nc)



for tc in range(1,11):
    T = input()
    arr = [list(map(int,input().split())) for _ in range(100)]


    st = -1
    en = -1
    visited = []
    for i in range(100):
        if arr[99][i] == 2:
            st,en = 99,i
    print('#{} {}'.format(tc,DFS(st,en)))



