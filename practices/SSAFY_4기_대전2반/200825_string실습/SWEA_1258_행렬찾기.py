#행렬의 사이즈를 찾는 함수
def search_size(r, c):
    r_cnt = 0
    c_cnt = 0

    for i in range(r, N + 2):
        if arr[i][c] == 0:
            break
        r_cnt += 1
    for j in range(c, N + 2):
        if arr[r][j] == 0:
            break
        c_cnt += 1

    ans.append([r_cnt, c_cnt])

    init(r, c, r_cnt, c_cnt)

#구한 행렬을 0으로 초기화 시키는것
def init(r, c, r_cnt, c_cnt):
    for i in range(r, r + r_cnt):
        for j in range(c, c + c_cnt):
            arr[i][j] = 0


T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    #전체적인 띠를 두르는 작업
    arr = [0] * (N + 2)
    arr[0] = arr[N + 1] = [0] * (N + 2)

    for i in range(N):
        arr[i + 1] = [0] + list(map(int, input().split())) + [0]

    ans = []

    for i in range(1, N + 2):
        for j in range(1, N + 2):
            if arr[i][j] != 0:
                search_size(i, j)

    #정렬, 행렬크기 기준, 같다면 행크기 기준
    ans = sorted(ans, key=lambda x: ((x[0] * x[1]), x[0]))

    print("#{} {}".format(tc, len(ans)), end=" ")
    for i in range(len(ans)):
        print("{} {}".format(ans[i][0], ans[i][1]), end=" ")

    print()
