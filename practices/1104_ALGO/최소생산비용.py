import sys
sys.stdin = open('최소생산비용.txt','r')


def backtracking(s,ans):
    if s == N :
        result.append(ans)
        return
    for i in arr[s]:
        backtracking(s+1,ans+i)
    return

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    result = []

    backtracking(0,ans)
    print(min(result))