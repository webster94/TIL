import sys
sys.stdin = open('배열돌리기3.txt','r')
# 함수를 만들어서 여러번돌릴 수 있게 만들자!
def one():
    global arr
    arr= arr[::-1]
def two():
    global arr
    for i in range(N):
        arr[i] = arr[i][::-1]
def three():
    global arr,N,M
    N,M = M,N
    temp = []
    for i in list(zip(*arr)):
        temp.append(list(i)[::-1])
    return temp
def four():
    global arr,N,M
    N,M = M,N
    temp = []
    for i in list(zip(*arr))[::-1]:
        temp.append(list(i))
    return temp
def rotate5():
    global arr, N, M
    n = N // 2
    m = M // 2
    temp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i < n and j < m:
                temp[i][j + m] = arr[i][j]
            elif i < n and j >= m:
                temp[i + n][j] = arr[i][j]
            elif i >= n and j >= m:
                temp[i][j - m] = arr[i][j]
            elif i >= n and j < m:
                temp[i - n][j] = arr[i][j]
    return temp
def rotate6():
    global arr, N, M
    temp = [[0]*M for _ in range(N)]
    n = N // 2
    m = M // 2
    for i in range(N):
        for j in range(M):
            if i < n and j < m:
                temp[i + n][j] = arr[i][j]
            elif i < n and j >= m:
                temp[i][j - m] = arr[i][j]
            elif i >= n and j >= m:
                temp[i - n][j] = arr[i][j]
            elif i >= n and j < m:
                temp[i][j + m] = arr[i][j]
    return temp


N,M,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dir = list(map(int,input().split()))

for d in dir:
    if d == 1:
        one()
    elif d == 2:
        two()
    elif d == 3:
        arr = three()
    elif d ==4:
        arr =four()
    elif d ==5:
        arr = rotate5()
    elif d ==6:
        arr= rotate6()


print(arr)
