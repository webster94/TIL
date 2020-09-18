def turn90(new):
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[j][N-i-1] = new[i][j]
    return arr

T = int(input())
for t in range(1,T+1):
    N = int(input())
    NEW = []
    for i in range(N):
        arr = input().split()
        NEW.append(arr)

    rotate90 = turn90(NEW)
    rotate180 = turn90(rotate90)
    rotate270 = turn90(rotate180)
    print("#{}".format(t))
    for i in range(N):
        a = ''.join(rotate90[i])
        b = ''.join(rotate180[i])
        c = ''.join(rotate270[i])
        print(f'{a} {b} {c}')