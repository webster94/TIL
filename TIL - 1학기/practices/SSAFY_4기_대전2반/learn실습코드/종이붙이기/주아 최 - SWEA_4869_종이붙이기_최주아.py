import sys
sys.stdin = open('input.txt', 'r')



def paper(N):

    if memo[N] == -1:
        memo[N] = paper(N - 1) + paper(N - 2) * 2

    return memo[N]

for T in range(1, int(input()) + 1):
    N = int(input())
    M = N // 10

    memo = [-1] * (M + 1)

    memo[1] = 1
    memo[2] = 3

    print('#{} {}'.format(T, paper(M)))