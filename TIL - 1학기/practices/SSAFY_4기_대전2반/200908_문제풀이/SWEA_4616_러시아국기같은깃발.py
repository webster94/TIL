T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 행과열
    # 각 행에 색 카운트
    w = [0] * N
    b = [0] * N
    r = [0] * N

    for i in range(N):
        color = input()
        w[i] = color.count('W')
        b[i] = color.count('B')
        r[i] = M - w[i] - b[i]  # M개에서 w의 개수 , b의 개수를 뺀값이 r의 개수

    # 누적합 구하기 ( 나중에 한번에 계산하기 위해서 )
    for i in range(1, N):
        w[i] += w[i - 1]
        b[i] += b[i - 1]
        r[i] += r[i - 1]

    ans = N * M
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            # 흰색 칠하기
            #i까지의 전체 개수를 구한뒤 지금까지 칠해져있는 화이트 개수를 빼기
            cnt = M * (i + 1) - w[i]
            # 파란색 칠하기
            #j-i를 해서 유의미한 전체의 개수를 뽑고 , b[j] - b[i]를 하여 해당 범위의 전체 파랑 개수를 뽑아내기
            cnt += M * (j - i) - (b[j] - b[i])
            # 빨간색 칠하기
            #위와 마찬가지... ㅎ
            cnt += M * (N-1 - j) - (r[N-1] - r[j])
            ans = min(ans, cnt)
    print("#{} {}".format(tc, ans))
