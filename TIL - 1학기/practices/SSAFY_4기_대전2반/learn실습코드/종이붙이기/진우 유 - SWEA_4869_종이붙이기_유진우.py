for tc in range(1, int(input()) + 1):
    N = int(input()) // 10

    f = [0] * (N + 1)
    f[1], f[2] = 1, 3

    for i in range(1, N+1):
        if f[i] == 0:
            f[i] = f[i-1] + 2*f[i-2]

    print('#{} {}'.format(tc, f[N]))