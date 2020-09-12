def check(M):
    for i in range(N):
        for j in range(N - M + 1):
            # 가로
            tmp = words[i][j:j + M]
            # 세로
            tmp2 = zwords[i][j:j + M]

            if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:
                return M

    return 0


for tc in range(10):
    tc_num = int(input())

    N = 100

    words = [list(input()) for _ in range(N)]
    zwords = list(zip(*words))

    for k in range(100, 0, -1):
        ans = check(k)
        if ans != 0:
            break

    print("#{} {}".format(tc_num, ans))
