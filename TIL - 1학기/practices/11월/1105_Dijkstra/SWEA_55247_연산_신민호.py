import sys
from collections import deque
sys.stdin = open('연산.txt','r')

def bfs(n):
    q = deque()
    q.append([n,0])
    while q:
        v,c = q.popleft()
        if v == M:
            return c
        for i in range(4):
            if i == 0 :
                if v+1 not in visit and 0<=v+1<1000001:
                    q.append((v+1, c + 1))
                    visit.append(v+1)
            if i == 1:
                if 0<=v-1<1000001 and v-1 not in visit:
                    q.append((v-1, c + 1))
                    visit.append(v+1)
            if i == 2 :
                if 0<=v*2<1000001 and v*2 not in visit:
                    q.append((v*2, c + 1))
                    visit.append(v*2)
            if i == 3 :
                if 0<=v-10<1000001 and v-10 not in visit:
                    q.append((v-10, c + 1))
                    visit.append(v-10)


T =  int(input())
for t in range(1,T+1):
    N , M = map(int,input().split())
    visit=[]
    result= bfs(N)
    print('#{} {}'.format(t,result))