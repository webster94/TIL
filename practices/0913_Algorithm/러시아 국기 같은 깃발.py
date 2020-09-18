import sys
sys.stdin = open("러시아.txt","r")
T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [input() for _ in range(N)]
    count = 0
    result = []
    white = 0
    for i in range(N-2):
        for a in range(M):
            if arr[i][a] != 'W':
                white += 1
        blue = 0
        for j in range(i+1,N-1):
            for a in range(M):
                if arr[j][a] != 'B':
                    blue += 1
            red = 0
            for k in range(j+1,N):
                for a in range(M):
                    if arr[k][a] != 'R':
                        red += 1
            result.append((white + blue + red))
    print("#{} {}".format(t,min(result)))
