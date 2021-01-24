T = int(input())
def back(s,k):
    if s == 7:
        print(visited)
    else:
        for i in range(s,8):
            if not visited[i]:
                visited[i] = 1
                back(s+1,k)
                visited[i] = 0



dr = [0,0,1,-1,1,1,-1,-1]
dc = [1,-1,0,0-1,1,1,-1]

for t in range(1,T+1):
    N = int(input())
    arr = [[0] * 8 for _ in range(8)]
    visited = [0] * 8
    back(0,0)