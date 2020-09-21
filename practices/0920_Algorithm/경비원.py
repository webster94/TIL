import sys
sys.stdin = open("경비원.txt","r")
dr = [0,-1,0,1]
dc = [-1,0,1,0]
garo,sero = map(int,input().split())
arr = [[0] * garo for _ in range(sero)]
store = int(input())
for t in range(store):
    D,P = map(int,input().split())
    if D == 1 :
        arr[0][P] = 1
    elif D == 2:
        arr[sero-1][P] = 1
    elif D == 3:
        arr[P][0] = 1
    elif D == 4:
        arr[P][garo-1] = 1

st,ed = map(int,input().split())
if st == 1:
    arr[0][ed] = 2
elif st == 2:
    arr[sero - 1][ed] = 2
elif st == 3:
    arr[ed][0] = 2
elif st == 4:
    arr[ed][garo - 1] = 2
count = 0
i =0
j = 0
d = 0
result = []
while True:
    nr = i + dr[d]
    nc = j + dc[d]
    if 0 <= nr < sero and 0 <= nc < garo and arr[nr][nc] == 0:
        i,j = nr,nc
        count += 1
    if arr[nr][nc] ==1:
        result.append(count)
        break
    else:
        d = (d+1)%4
        i = i + dr[d]
        j = j + dc[d]
print(result)