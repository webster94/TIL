import sys
sys.stdin = open("input.txt","r")

def dfs():
    stack.append(S)
    while len(stack)!=0:
        v = stack.pop()
        if v == G:
            return 1
        if v not in visited:
            visited.append(v)
            for w in link[v]:
                stack.append(w)
    else:return 0

for t in range(1,int(input())+1):
    V,E = map(int,input().split())
    link = [[] for _ in range(V+1)]
    stack = []
    visited = [False]*(V+1)
    for i in range(E):
        n1,n2 = map(int,input().split())
        link[n1].append(n2)
    S,G = map(int,input().split())
    print('#{} {}'.format(t,dfs()))
