#상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

drc = [[-1,0],[1,0],[0,-1],[0,1]]


r = 1
c = 1

for i in range(4):
    nr = r+dr[i]
    nc = c +dc[i]

    print(nr, nc)

#############################################
nums = [[1,2,3]
       ,[4,5,6],
        [7,8,9]]

r = 0
c = 1


dr = [-1,1,0,0]
dc = [0,0,-1,1]

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    # 1. 범위를 벗어나면 수행하지 않겠다.
    if nr<0 or nr >= 3 or nc < 0 or nc>=3:
        continue
    print(nums[nr][nc])
    #2. 범위 안에 들어왔을때만 수행하겠다.
    # if 0 <= nr <3 and 0<= nc <3:
    #     print(nums[nr][nc])