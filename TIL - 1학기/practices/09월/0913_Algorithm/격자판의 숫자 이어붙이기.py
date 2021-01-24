import sys
sys.stdin = open("격자판.txt","r")
def dfs(a,b,k,char):
    char += str(arr[a][b])
    if k == 6:
        total.add(char)
        return total
    for n in range(4):
        nr = a + dr[n]
        nc = b + dc[n]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr,nc,k+1,char)




T= int(input())
for t in range(1,T+1):
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    result = set()
    arr = [list(map(int,input().split())) for _ in range(4)]
    char = ''
    total = set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,0,char)

    print("#{} {}".format(t,len(total)))
