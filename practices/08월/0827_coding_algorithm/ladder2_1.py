import sys
import copy
sys.stdin = open("ladder2.txt.txt", "r")
dr = [0,0,1]
dc = [1,-1,0]
# 시작점으로바꾸고
# 최소거리랑 최소거리인 시작점을 변수에 할당
# 최소거리 > DFS가 작은 그 좌표를 ans에 저장하고
# ans 출력한다.1
def DFS(a,b):
    # 재귀의 종료조건!
    # arr2[a][b] = 0 # 방문체크
    visited.append([a,b])
    if a == 99:
        return len(visited)
    for k in range(3):
        nr = a + dr[k]
        nc = b + dc[k]
        if nr < 0 or nc < 0 or nr >= 100 or nc >= 100:
            continue
        if arr[nr][nc] != 1 and visited:
            continue
        if [nr,nc] in visited:
            continue
        return DFS(nr,nc)






for tc in range(1,11):
    N = input()
    arr = [list(map(int,input().split())) for _ in range(100)]
    result = []
    # 입력받았음.
    # 사다리는 시작에서 끝지점을 찾아야지
    for i in range(100):
        st,en = -1,-1
        if arr[0][i] == 1:
            st,en = 0,i
            visited = []
            result.append([en,DFS(st,en)])
            # arr2 = arr[:]
            # print("#{} {}".format(tc,DFS(st,en)))
    result.sort(key=lambda x: (x[1], -x[0]))
    # print(result)
    print("#{} {}".format(tc, result[0][0]))