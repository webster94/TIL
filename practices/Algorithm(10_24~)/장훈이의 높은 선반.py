import sys
sys.stdin = open('장훈이의 높은 선반.txt','r')

def powerset(idx,b):
    total = 0
    result = []
    global ans
    if idx == N: # 끝에 다다르면
        for i in range(N): # N의 범위에서
            if visited[i]: # visited[N] = 1 이라면
                total += heights[i] # 토탈에 그 숫자를 더한다.
        result.append(total-b)
        for k in range(len(result)):
            if result[k] >= 0 and ans >= result[k]:
                ans = result[k]
        return # 꼭 있어야행

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
    ans = 9999999
    powerset(0,B)
    print('#{} {}'.format(t,ans))