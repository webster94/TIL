arr = [ [1,2,3],
        [4,5,6,],
        [7,8,9]
       ]
N = len(arr)
M = len(arr[0])
#
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j], end=' ')
#     print()
# print()

for j in range(M):  # 열을 먼저돌렸다
    for i in range(N):
        print(arr[i][j], end=' ')
    print()
print()