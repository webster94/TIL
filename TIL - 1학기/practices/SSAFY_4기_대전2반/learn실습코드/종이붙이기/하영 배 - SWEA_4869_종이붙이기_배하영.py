T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dp = []
    dp.append(1)
    dp.append(3)
    for n in range(2, N // 10):
        dp.append(dp[n - 1] + dp[n - 2] * 2)
    print('#{} {}'.format(tc, dp[N // 10 - 1]))