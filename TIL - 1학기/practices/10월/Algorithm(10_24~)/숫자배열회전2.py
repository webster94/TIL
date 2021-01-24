import sys
sys.stdin = open('숫자배열회전.txt','r')

def rotate1(arr):
    arr_new = []
    arr = arr[::-1]
    for i in list(zip(*arr)):
        arr_new.append(list(i))
    return arr_new

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr0 = [list(input().split()) for _ in range(N)]
    arr90 = rotate1(arr0)
    arr180 = rotate1(arr90)
    arr270 = rotate1(arr180)
    print('#{}'.format(t))
    for i in range(N):
        arr90[i] = ''.join(arr90[i])
        arr180[i] = ''.join(arr180[i])
        arr270[i] = ''.join(arr270[i])
        print('{} {} {}'.format(arr90[i],arr180[i],arr270[i]))
