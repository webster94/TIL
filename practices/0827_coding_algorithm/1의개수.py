dr = [0,1,0,-1]
dc = [1,0,-1,0]
N = int(input())
# 입력 받아서
arr = []
for _ in range(N):
    sen = list(map(int,input()))
    arr.append(sen)
d = 0
r = 0
c = 0
num = 1
count = 0
while(True):
    arr[r][c] = num
    nr = r + dr[d]
    nc = c + dc[c]

    if 0 <= nc < N and 0 <= nr < N and arr[r][c] == 0:
        r,c = nr,nc
        count +=1
    else:
        d = (d+1)%4
        r += dr[d]
        c += dc[d]
print(count)


