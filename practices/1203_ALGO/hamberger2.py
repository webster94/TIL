import sys
sys.stdin = open('hamberger.txt','r')
def dfs(index, sum_flavor = 0 , sum_cal = 0):
    global max_flavor
    if sum_cal > L: return
    if max_flavor < sum_flavor: max_flavor=sum_flavor
    if index == N: return
    flavor,cal = arr[index]
    dfs(index+1, sum_flavor+flavor, sum_cal+cal)
    dfs(index+1,sum_flavor,sum_cal)

T = int(input())
for t in range(1,T+1):
    N,L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_flavor = 0
    dfs(0)
    print('#{} {}'.format(t,max_flavor))