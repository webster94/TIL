import sys

sys.stdin = open('배틀필드.txt', 'r')

move_list = {'U': 0, 'D': 1, 'L': 2, 'R': 3, 'S': 4, '^': 0, 'v': 1, '<': 2, '>': 3, 0 : '^',1:'v',2:'<',3:'>'}
movement = ['^', 'v', '<', '>']
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for t in range(1, T + 1):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    # 출발점 찾기
    for i in range(H):
        for j in range(W):
            if arr[i][j] in movement:
                tank_pos = [i, j, move_list[arr[i][j]]]
                break
            else:
                continue
    # 출발점 찾았다
    # 명령어대로 움직이자
    L = int(input())
    commands = list(input())
    for command in commands:
        # S의 경우 대비
        dir = move_list[command]
        if dir == 4:
            nr = tank_pos[0]
            nc = tank_pos[1]
            while True:

                nr += dr[tank_pos[2]]
                nc += dc[tank_pos[2]]
                if nr < 0 or nr >= H or nc < 0 or nc >= W or arr[nr][nc] == '#':
                    break
                if arr[nr][nc] == '*':
                    arr[nr][nc] = '.'
                    break
        else:
            r = tank_pos[0]
            c = tank_pos[1]
            arr[r][c] = move_list[dir]
            nr = r + dr[dir]
            nc = c + dc[dir]
            tank_pos = (r,c,move_list[command])
            if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] == '.':
                arr[r][c] = '.'
                arr[nr][nc] = move_list[dir]
                tank_pos = [nr,nc,dir]
    print('#{}'.format(t), end=" ")
    for m in arr:
        print(''.join(m))
