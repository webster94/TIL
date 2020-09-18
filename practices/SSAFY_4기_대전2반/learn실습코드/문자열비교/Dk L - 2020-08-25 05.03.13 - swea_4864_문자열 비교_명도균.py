for test_case in range(1, int(input()) + 1):
    N = list(input())
    M = list(input())
    n = len(N)
    m = len(M)
    result = 0
    for x in range(m-n+1):
        if N == M[x:x+n]:
            result = 1
    print(f'#{test_case} {result}')


    