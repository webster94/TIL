#왼쪽 오른쪽
dc = [-1, 1]


def dir_check(r, c):
    for i in range(2):
        nc = c + dc[i]
        if 0 <= nc < 100 and ladder[r][nc] == 1:
            return i
    #왼쪽 오른쪽 걸리지 않으면 2를 리턴
    return 2


def go(st):
    col = st_pos[st]
    cnt = 0
    idx = st
    #아래로 100칸 이동
    for i in range(100):
        d = dir_check(i, col)
        if d < 2:
            #인덱스위치 개선
            idx += dc[d]
            #한번에 이동
            cnt += abs(col - st_pos[idx])
            #현재 사다리 갱신
            col = st_pos[idx]
        #아래로 한칸이동
        cnt += 1

    #현재까지 구한 답 리턴
    return cnt


for tc in range(10):
    # 테스트케이스 번호 입력
    tc_num = int(input())

    # 2차원 리스트 입력
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 시작 좌표를 담을 리스트
    st_pos = []
    # 시작 좌표를 다 담았다.
    for i in range(100):
        if ladder[0][i] == 1:
            st_pos.append(i)

    # 임의의 큰값으로 초기화
    min_value = 987654321
    # 어차피 정답으로 사용될거니 안쓰이는수 아무거나로 초기화
    ans_idx = -1

    for i in range(len(st_pos)):
        tmp = go(i)

        if tmp <= min_value:
            min_value = tmp
            ans_idx = st_pos[i]

    print("#{} {}".format(tc_num, ans_idx))
