T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    w = [0] * N
    b = [0] * N
    r = [0] * N

    for i in range(N):
        color = input()
        w[i] = color.count('W')
        b[i] = color.count('B')
        r[i] = M -w[i] -b[i] # 각행에 M 개에서 w의 개수, b의 개수를 뺀 값이 r의 개수

    for i in range(1,N):
        w[i] +=w[i-1]
        b[i] += b[i-1]
        r[i] += r[i-1] # 누적합을 구해놓은 상태
    ans = N*M
    for i in range(N-2):
        for j in range(i+1,N-1):
            # 흰색 칠하기
            cnt = M * (i+1) - w[i]
            # 파란색 칠하기
            cnt += M * (j-1) - (b[j] - b[i]) # M * J-1 전체칸을 구하는 식
            # 빨간색 칠하기
            cnt += M * (N-1 - j) - (r[N-1] - r[j])
            ans = min(ans,cnt)

    print("#{} {}".format(tc,ans))