import sys
sys.stdin=open('1873.상호의 배틀필드.txt','r')
move_list= [(-1,0),(1,0),(0,1),(0,-1)]
command_dict = {'U':0,'D':1,'R':2,'L':3,'S':4, '^':0, 'v':1,'>':2,
                '<':3,0 : '^',1:'v',2:'>',3:'<'}
search_list = ['^','v','>','<']
T = int(input())
for t in range(1,T+1):
    H,W = map(int,input().split())
    arr = [list(input()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if arr[i][j] in search_list:
                tank_pos = (i,j,command_dict[arr[i][j]])
                break
            else:
                continue
    # print(tank_pos) 위치 찾기 완료
    length = int(input())
    move = list(input())
    for i in move:
        temp = command_dict[i]
        if temp == 4:
            dr = tank_pos[0]
            dc = tank_pos[1]
            while True:
                dr += move_list[tank_pos[2]][0]
                dc += move_list[tank_pos[2]][1]
                if dr < 0 or dc < 0 or dr >= H or dc >= W or arr[dr][dc]== '#':
                    break
                if arr[dr][dc] == '*':
                    arr[dr][dc] = '.'
                    break
        else:
            y = tank_pos[0]
            x = tank_pos[1]
            dr = y+ move_list[temp][0]
            dc = x + move_list[temp][1]
            arr[y][x] = command_dict[temp]
            tank_pos = (y,x,temp)
            if 0 <= dr < H and 0 <= dc < W and arr[dr][dc] == '.':
                arr[y][x] = '.'
                arr[dr][dc] = command_dict[temp]
                tank_pos = (dr,dc,temp)
    print('#{}'.format(t),end= " ")
    for m in arr:
        print(''.join(m))
