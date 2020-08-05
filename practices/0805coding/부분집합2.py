def partsum(list):

    N = len(list)
    cnt = 0
    for i in range(1<<N):  # 1을 열칸 옮겼다.
        SUM = 0
        sub = []
        for j in range(N):
            if i & (1 << j):
                sub.append(list[j])
                SUM += list[j]
                if SUM > 0:
                    break
        if SUM == 0:
            cnt +=1
            print(sub)

data = list(map(int, input().split()))
partsum(data)