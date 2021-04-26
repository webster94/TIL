def answer(arr):
    for i in range(N):
        for j in range(1):
            print(arr2[i][j], arr2[i][j + 1])
import sys
N =int(input())

arr = []
arr2 = []
for _ in range(N):
    arr.append((sys.stdin.readline().split()))
for i in range(N):
    for j in range(1):
        arr2.append((int(arr[i][j]),arr[i][j+1]))
arr2 = sorted(arr2, key=lambda arr2:arr2[0])
answer(arr2)
# arr2 =sorted(arr2, key=lambda arr2:arr2[0])
# Lambda 사용 법 :
# 솔티드 하고 key 람다로 설정해주고 어레이를 정렬할 부분을 넣어준다! : 로!