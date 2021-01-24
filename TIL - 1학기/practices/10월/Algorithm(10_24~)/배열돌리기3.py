import sys
sys.stdin = open('배열돌리기3.txt','r')

# def rotate(d,r):
#     arr_new = [[0] * M for _ in range(N)]
#     if d == 1:
#         for i in range(N):
#             for j in range(M):
#                 arr_new[N-1-i][j] = arr[i][j]
#         return arr_new
#     elif d ==2:
#         for i in range(N):
#             for j in range(M):
#                 arr_new[i][M-1-j] = arr[i][j]
#         return arr_new
#     elif d == 3:
#         arr_new = [[0] * N for _ in range(M)]
#         for i in range(N):
#             for j in range(M):
#                 arr_new[j][N-1-i] = arr[i][j]
#         return arr_new
#     elif d == 4:
#         arr_new = [[0] * N for _ in range(M)]
#         for i in range(N):
#             for j in range(M):
#                 arr_new[M-j-1][i] = arr[i][j]
#         return arr_new
#     elif d == 5 :
#         print(N, M, '여기나오나')
#         n = N//2
#         m =  M//2
#         for i in range(N):
#             for j in range(M):
#                 if i < n and j < m:
#                     arr_new[i][j+m] = arr[i][j]
#                 elif i < n and j >= m:
#                     arr_new[i+n][j] = arr[i][j]
#                 elif i >=n and j >= m:
#                     arr_new[i][j-m] = arr[i][j]
#                 elif i >= n and j < m:
#                     arr_new[i-n][j] = arr[i][j]
#         return arr_new
#     elif d == 6 :
#         n = N//2
#         m =  M//2
#         for i in range(N):
#             for j in range(M):
#                 if i < n and j < m:
#                     arr_new[i+n][j] = arr[i][j]
#                 elif i < n and j >= m:
#                     arr_new[i][j-m] = arr[i][j]
#                 elif i >=n and j >= m:
#                     arr_new[i-n][j] = arr[i][j]
#                 elif i >= n and j < m:
#                     arr_new[i][j+m] = arr[i][j]
#         return arr_new
def rotate1():
    global arr,N,M
    arr = arr[::-1]
def rotate2():
    global arr, N, M
    for i in range(N):
        arr[i] = arr[i][::-1]
def rotate3():
    global arr, N, M
    N,M = M,N
    temp = []
    for i in list(zip(*arr)): # 시계방향으로 90도 돌린 걸 리스트화
        temp.append(list(i)[::-1]) # 거꾸로 temp에 복사
    return temp
def rotate4():
    global arr,N,M
    N,M = M,N
    temp = []
    arr = list(zip(*arr))
    for i in range(N-1,-1,-1):
            temp.append(list(arr[i]))
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
d = list(map(int,input().split()))
for k in d:
    if k ==1 :
        rotate1()
    if k ==2 :
        rotate2()
    if k ==3 :
        arr = rotate3()
    if k ==4 :
        arr = rotate4()
    if k ==5 :
        arr = rotate5()
    if k ==6 :
        arr = rotate6()
for i in range(N):
    for j in range(M):
        print(arr[i][j], end = ' ')
    print()