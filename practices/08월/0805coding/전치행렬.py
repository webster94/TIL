'''3 3
1 2 3
4 5 6
7 8 9
'''
# N, M = map(int,input().split())
# mylist = [0 for _ in range(N)]
# # mylist = [0]*N
# for i in range(N):
#     mylist[i] = list(map(int,input().split()))
# print(mylist)
#2 list comprehension
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(i+1,M):
        if i<j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for j in range(i+1, len(arr)):
        print((arr[i],arr[j],end = ' '))
print(arr)
# 0으로 초기화
# N = 3
# M = 4
# v = [[0 for _ in range(M)] for _ in range(N)] # 행을 먼저써야한다
# print(v)
#  # 방법2
# v = [[0]*M for _ in range(N)]
# print(v)