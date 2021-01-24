import sys
sys.stdin = open('추억의2048게임.txt','r')
key = {'up': 0 ,'down':1, 'left': 2, 'right':3}

def push():
    for i in range(N):
        stack = []
        for j in range(N-1,-1,-1):
            if arr[j][i]:
                stack.append(arr[j][i])
                arr[j][i] = 0
        idx = 0
        while stack:
            if len(stack) > 1:
                A,B = stack.pop(), stack.pop()
                if A==B:
                    arr[idx][i] = A + B
                else:
                    arr[idx][i] = A
                    stack.append(B)
                idx +=1
            else:
                arr[idx][i] = stack.pop()

def rotation(arr):
    tmp = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            tmp[i][j] = arr[N-1-j][i]
    return tmp

T = int(input())
for t in range(1,T+1):
    N,S = input().split()
    N = int(N)
    arr = [list(map(int,input().split())) for _ in range(int(N))]
    if key[S] == 0:
        push()
    elif key[S] == 1:
        arr = rotation(arr)
        arr = rotation(arr)
        push()
        arr = rotation(arr)
        arr = rotation(arr)

    elif key[S] == 2:
        arr = rotation(arr)
        push()
        arr = rotation(arr)
        arr = rotation(arr)
        arr = rotation(arr)
    elif key[S] == 3:
        arr = rotation(arr)
        arr = rotation(arr)
        arr = rotation(arr)
        push()
        arr = rotation(arr)

    print("#{}".format(t))
    for i in range(N):
        print(*arr[i])