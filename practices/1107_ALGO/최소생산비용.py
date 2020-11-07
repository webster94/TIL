import sys
sys.stdin = open('최소생산비용.txt','r')
def check(visited,idx,result):
    global ans
    if result > ans:
        return
    if visited == (1<<N) -1:
        ans = min(ans,result)
        return

    for i in range(N):
        if (1<<i) & visited : continue
        check((1<<i) | visited , idx+1, result+cost[idx][i])

T = int(input())
for t in range(1,T+1):
    N = int(input())
    cost = [list(map(int,input().split())) for _ in range(N)]
    ans = 0xfffffffff
    for i in range(N):
        check((1<<i),1,cost[0][i])
    print("#{} {}".format(t,ans))