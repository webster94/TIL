# def f(n):
#     if n == 10:
#         return 1
#     elif n == 20:
#         return 3
#     return f(n-10) + (2*f(n-20))
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     print('#{} {}'.format(tc, f(N)))


# 다른 풀이
def f(N):
    global memo
    if N >=3 and len(memo) <= N:
        memo.append(f(N-1) + (f(N-2)*2))
    return memo[N]

T = int(input())
for tc in range(1,T+1):
    N = int(input())//10
    memo = [0, 1, 3]
    print('#{} {}'.format(tc, f(N)))