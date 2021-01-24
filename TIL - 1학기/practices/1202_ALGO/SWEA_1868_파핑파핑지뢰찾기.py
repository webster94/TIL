from _collections import deque
import sys
sys.stdin = open('1868.파핑파핑 지뢰찾기.txt','r')

def clickornot(x,y):
    global cnt
    next_target = []
    for k in range(8):
        nr = x + dr[k]
        nc = y + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == '.':
                next_target.append((nr,nc))
            elif arr[nr][nc] == '*':
                break
    else:
        if next_target:
            arr[x][y] = 'o'
            cnt += 1
            spread(next_target)

def spread(lst):
    q = deque(lst)
    while q:
        x,y = q.popleft()
        arr[x][y] = 'o'
        next_next_target = []
        for k in range(8):
            nr = x + dr[k]
            nc = y + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == '.':
                    next_next_target.append((nr,nc))
                elif arr[nr][nc] == '*':
                    break
        else:
            spread(next_next_target)

def restTarget():
    global cnt
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.':
                cnt +=1


dr = [1,1,-1,-1,0,0,1,-1]
dc = [1,-1,-1,1,1,-1,0,0]
T= int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.':
                clickornot(i,j)
    restTarget()
    print('#{} {}'.format(t,cnt))