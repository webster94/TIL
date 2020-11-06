import sys
sys.stdin = open('최소비용.txt','r')

def bfs():
    print(dist)
T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dist = [[984321332] * N for _ in range(N)]
    bfs()