# BFS로 풀고 마지막 숫자 중에서 최대값을 뽑아야하네..?
import sys
sys.stdin = open("컨택.txt.py","r")
def BFS(n):
    q = []
    q.append(n)
    while q:
        for k in list_adj:
            if k not in visit:
                q.append(k)
                visit[k] = 1
                result += str(k)


for t in range(1):
    N,st = map(int,input().split())
    list_adj = [[] * (N+1) for _ in range(N+1)]
    arr = list(map(int,input().split()))
    visit = [] * (N+1)
    result = ''
    for i in range(0,N,2):
        p,c = arr[i],arr[i+1]
        list_adj[p].append(c)
   BFS(st)
   print(result)
