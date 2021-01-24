for tc in range(1,11):
    N = int(input())
    arr = [input().split() for _ in range(N) ]

    ans = 0

    for i in range(N):
        #내가 만나야될 컬러
        state = 1
        for j in range(N):
            #내가 빨강을 만나야하고 마침 내자리가 빨강이라면
            if state==1 and arr[j][i] == '1':
                state = 2
            #내가 파랑을 만나야하고 마침 내자리가 파랑이면 교착상태 1증가
            elif state == 2 and arr[j][i] == '2':
                state = 1
                ans += 1

    print("#{} {}".format(tc, ans))