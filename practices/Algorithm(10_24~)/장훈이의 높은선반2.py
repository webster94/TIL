import sys
sys.stdin = open('장훈이의 높은 선반.txt','r')

def powerset(idx,b):
    global ans
    result = []
    total = 0
    if idx == N:
        for i in range(N):
            if visited[i]:
                total += heights[i]
        if 0 <= total - b <= ans:
            ans = total - b
        return



    else:
        visited[idx] = 1
        powerset(idx+1,b)
        visited[idx] = 0
        powerset(idx+1,b)

T = int(input())
for t in range(1,T+1):
    N,B = map(int,input().split())
    heights = list(map(int,input().split()))
    visited = [0] * N
    ans = 143783289523
    powerset(0,B)
    print('#{} {}'.format(t,ans))