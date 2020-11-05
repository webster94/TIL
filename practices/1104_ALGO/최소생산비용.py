import sys
sys.stdin = open('최소생산비용.txt','r')


def backtracking(visited, idx, result):
    if result > ans:
        return
    if visited == (1<<N) -1  :
        ans = min(ans,result)
        return

    for i in range(N):
        if visited & (1<<i) : continue

        backtracking(visited | 1 << i , idx + 1 , result + arr[idx][i])
    return

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0xffffff
    for i in range(N): # 첫번째 공장에서 모든 경우의 수를 확인해보아야함
        backtracking(1<<i,i,arr[0][i])
    print(min(result))