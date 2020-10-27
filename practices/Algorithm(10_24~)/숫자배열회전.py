import sys
sys.stdin = open('숫자배열회전.txt','r')

def rotate(arr):
    arr_new = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_new[j][N-i-1] = arr[i][j]
    return arr_new

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        numbers = input().split()
        arr.append(numbers)
    arr90 = rotate(arr)
    arr180 = rotate(arr90)
    arr270 = rotate(arr180)
    print('#{}'.format(t))
    for i in range(N):
        atr90 = ''.join(arr90[i])
        atr180 = ''.join(arr180[i])
        atr270 = ''.join(arr270[i])
        print(atr90,atr180,atr270)



