import sys
sys.stdin = open("faltten.txt","r")
for t in range(1,11):
    N = int(input())
    arr = list(map(int,input().split()))
    while N>0 :
        x = arr.index(max(arr))
        y = arr.index(min(arr))
        arr[x] = arr[x] - 1
        arr[y] = arr[y] + 1
        N -= 1
    print("#{} {}".format(t,max(arr) - min(arr)))