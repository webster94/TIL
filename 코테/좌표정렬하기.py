import sys
N = int(input())

arr = []
for _ in range(N):
    a,b= map(int,sys.stdin.readline().split())
    arr.append((b,a))
arr = sorted(arr)
for i in range(N):
    for j in range(1):
        print(arr[i][j+1], arr[i][j])