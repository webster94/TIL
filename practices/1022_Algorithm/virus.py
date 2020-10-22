import sys
sys.stdin = open('virus.txt','r')
def dfs(n):
    global count
    visited[n] = 1
    # print(n,end = ' ')
    for k in range(1,c_nums+1):
        if visited[k] ==0 and arr[n][k] == 1:
            dfs(k)
            count += 1


c_nums = int(input())
M = int(input())
arr = [[0] * (c_nums+1) for _ in range(c_nums+1)]
visited = [0] * (c_nums+1)
# print(visited)
for _ in range(M):
    st,ed = map(int,input().split())
    arr[st][ed] = arr[ed][st] = 1
count = 0
dfs(1)
print(count)
