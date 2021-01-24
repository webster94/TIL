arr = [1,2,3] # 원본
N = 3 # 원본의 줄
sel = [0] * N # 나열할 공간
visited = [0] * N # 저장공간?

def perm(idx): # 깊이를 호출
    if idx == N: # 같을 경우 호출
        print(sel) #
        return
    for i in range(N): #
        if not visited[i]: # visited 가 0일 경우
            sel[idx] = arr[i] # sel[idx] 에다가 arr[i]를 넣는다.
            visited[i] = 1 # 방문표시를 하고
            perm(idx+1)  #   여긴 그려봐야한다..
            visited[i] = 0
perm(0)