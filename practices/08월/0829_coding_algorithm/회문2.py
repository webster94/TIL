import sys
sys.stdin = open("input (31).txt",'r')
def check(i):
    for a in range(100):
        for b in range(100-i+1):
            tmp = arr[a][b:b+i]
            tmp2 = zarr[a][b:b+i]

            if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:
                return i
    return 0

            # if arr[a][b:b+i] == arr[a][b:b+i][::-1]:
            #     return i
            # if zarr[a][b:b+i] == zarr[a][b:b+i][::-1]:
            #     return i


for t in range(1,11):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    #입력 받았음
    garo = []
    # print(arr)
    zarr = list(zip(*arr))
    for i in range(100,0,-1):
        ans = check(i)
        if ans != 0:
            break
    print("#{} {}".format(t,ans))