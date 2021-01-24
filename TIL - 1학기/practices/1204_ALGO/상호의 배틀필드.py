import sys
sys.stdin = open('배틀필드.txt','r')

move_list = {'U':0,'D':1,'L':2, 'R':3,'S':4, '^':0,'v':1,'<':2,'>':3, 0:'^',1:'v',2:'<',3:'>'}
move = ['^','v','<','>']
dr = [-1,1,0,0]
dc = [0,0,-1,1]
T = int(input())
for t in range(1,T+1):
    H,W = map(int,input().split())
    arr = [list(input()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if arr[i][j] in move:
                tank_pos = (i,j,move_list[arr[i][j]])
    L =int(input())
    commands = list(input())
    for command in commands:
        if move_list[command] == 4:
            nr = tank_pos[0]
            nc = tank_pos[1]
            dir = tank_pos[2]
            while True:
                nr += dr[dir]
                nc += dc[dir]
                if nr < 0 or nc < 0 or nr >= H or nc >= W or arr[nr][nc] == '#':
                    break
                if arr[nr][nc] == '*':
                    arr[nr][nc] = '.'
                    break
        else:
            r = tank_pos[0]
            c = tank_pos[1]
            dir = move_list[command]
            arr[r][c] = move_list[dir]
            nr = r +dr[dir]
            nc = c +dc[dir]
            tank_pos= (r,c,dir)
            if 0<= nr < H and 0<= nc < W and arr[nr][nc] == '.':
                tank_pos = (nr,nc,move_list[dir])
                arr[r][c] = '.'
                arr[nr][nc] = move_list[dir]
                tank_pos = (nr,nc,dir)

    print('#{}'.format(t) , end = ' ')
    for i in arr:
        print(''.join(i))