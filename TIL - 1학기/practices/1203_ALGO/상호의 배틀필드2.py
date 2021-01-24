import sys
sys.stdin = open('배틀필드.txt', 'r')
movement = ['^','v','<','>']
move_list = {'^':0, 'v':1, '<':2, '>':3,'U':0,'D':1,'L':2,'R':3,'S':4, 0:'^',1:'v',2:'<',3:'>'}
commands_list = ['U','D','L','R','S']
dr = [-1,1,0,0]
dc = [0,0,-1,1]

T = int(input())
for t in range(1,T+1):
    H,W = map(int,input().split())
    arr = [list(input()) for _ in range(H)]
    # start를 찾자
    for i in range(H):
        for j in range(W):
            if arr[i][j] in movement:
                tank_pos = (i,j,movement.index(arr[i][j]))
    # start  찾기 완료
    L =int(input())
    commands = list(input())
    # 포탄 먼저
    for command in commands:
        if move_list[command] == 4:
            nr = tank_pos[0]
            nc = tank_pos[1]
            dir = tank_pos[2]
            while True:
                nr += dr[dir]
                nc += dc[dir]
                if nr < 0 or nc < 0 or nr >= H or nc >=W or arr[nr][nc]=='#':
                    break
                if arr[nr][nc] == '*':
                    arr[nr][nc] = '.'
                    break
        else:
            r = tank_pos[0]
            c = tank_pos[1]
            dir = move_list[command]
            arr[r][c] = move_list[dir]
            nr = r + dr[dir]
            nc = c + dc[dir]
            tank_pos = (r,c,dir)
            if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] =='.':
                arr[r][c] = '.'
                arr[nr][nc] = move_list[dir]
                tank_pos = (nr,nc,dir)
    print('#{}'.format(t), end=' ')
    for m in arr:
        print(''.join(m))






