import sys
sys.stdin = open('숨바꼭질.txt','r')
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    while q:
        n= q.popleft()
        if n == K:
            return dist[n]
        for i in (n-1,n+1,2*n):
            if 0<= i <= 100000 and dist[i] == 0:
                q.append(i)
                dist[i] = dist[n]+1

N,K = map(int,input().split())
dist = [0] *100001
print(bfs(N))