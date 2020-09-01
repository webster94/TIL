#반복문 버전
import sys
sys.stdin = open('')
dc = [-1,1]
def dir_check(r,c):
    for i in range(2):
        nc  = c +dc[i]
        if 0 <= nc < 100 and ladder[r][nc] == 1:
            return i
    return 2 # ??

def go(st):
    col = st_pos[st]
    cnt = 0
    idx = st
    for i in range(100):
        d = dir_check[i,col]
        if d <2 :
            idx += dc[d]
            cnt += abs(col - st_pos[idx])
            col = st_pos[idx]
        cnt += 1
for tc in range(10):
    tc_num = int(input())

    ladder = [list(map(int,input().split())) for _ in range(100)]

    st_pos = []
    for i in range(100):
        if ladder[0][i] == 1
            st_pos.append(i)

    min_value = 987654321
    ans_idx = -1

    for i in range(len(st_pos)):
        tmp = go(i)

        if tmp <= min_value:
            min_value = tmp
            ans_idx = st_pos[i]

    print("#{} {}".format(tc_num,ans_idx))