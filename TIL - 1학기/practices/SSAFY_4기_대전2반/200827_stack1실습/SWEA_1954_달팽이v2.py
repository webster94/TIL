T = int(input())

for tc in range(1, T+1):
    N = int(input())

    nums = [[0]*N for _ in range(N)]

    K = N #이동거리
    d = 1 #방향
    row = 0 #행
    col = -1 #열 (초기에는 수평이동이므로 -1)
    num = 1 #넣을 값

    while True:
        #수평이동
        for c in range(K):
            col += d
            nums[row][col] = num
            num+=1
        #수평이동 끝 이제 수직이동
        K -= 1
        if K == 0:
            break
        #수직이동
        for r in range(K):
            row += d
            nums[row][col] = num
            num +=1
        #수직이동이 끝 수평이동
        d *= -1

    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(nums[i][j], end=" ")
        print()