# 8방향 델타
# 우, 우하, 하 좌하, 좌, 좌상, 상, 우상
dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]


def init():
    mid = N // 2
    othello[mid][mid] = othello[mid + 1][mid + 1] = 2
    othello[mid + 1][mid] = othello[mid][mid + 1] = 1

def change(r,c, color):
    #새로운 좌표에 돌은 놓았다.
    othello[r][c] = color

    #8방향 탐색
    for i in range(8):
        nr = r
        nc = c

        #해당 방향으로 break가 걸리기전까지 무조건 전진
        while True:
            nr += dr[i]
            nc += dc[i]
            #맵의 범위를 벗어났다면 그만
            if nr <= 0 or nr >N or nc <=0 or nc>N:
                break
            if othello[nr][nc] == 0:
                break
            if othello[nr][nc] == color:
                #같은 색깔을 만났으면 돌아나오면서 색칠하기
                while not(nr == r and nc == c):
                    nr -= dr[i]
                    nc -= dc[i]
                    othello[nr][nc] = color
                break


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    othello = [[0] * (N + 1) for _ in range(N + 1)]

    init()

    for i in range(M):
        c, r, color = map(int, input().split())
        change(r,c, color)

    b_cnt = 0
    w_cnt = 0

    for i in range(N+1):
        b_cnt += othello[i].count(1)
        w_cnt += othello[i].count(2)

    print("#{} {} {}".format(tc, b_cnt, w_cnt))