import sys; sys.stdin = open()
# 점화식을 찾는다. 가장 중요 문제의 푸는 방법을 찾는다. 작은문제와 큰문제와의 관계
def f(n): # n : 문제의 크기(식별값)
    #기저사례
    if n ==1: return 1
    if n ==3: return 3
    # 일반 사례
    if memo[n]: return memo[n]
    memo[n] = f(n-1) + f(n-2)*2
    return memo[n]
for tc in range(1,int(input())+1):
        N = int(input()) // 10
        memo = [0] * (N + 1)
        print(f(N))