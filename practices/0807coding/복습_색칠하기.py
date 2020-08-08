
for tc in range(1,int(input()) +1 ):
    N = int(input())
    arr = [[0] * 10 for _ in ragne(10)]

    for i in range(N):
        x1,y1,x2,y2,color = map(int,input().spilt())  # 바로 입력을 받네

        for i in range(x1,x2+1): # 바로 열에 ㄴ대입!
            for j in range(y1,y2+1):
                if arr[i][j] == 0 :
                    arr[i][j] += color

    for 1st in arr:
        print(*1st)

#