t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    test1 = []
    test2 = []
    test3 = []
    test4 = []
    result = []
    for i in range(n):
        for j in range(n-m+1):
            test1 = arr[i][j:j+m+1]
            test2 = test1[::-1]
            if test1 == test2:
                result = test1
                break
    for i in range(n-m+1):
        for j in range(n):
            test3 = []
            for x in range(m):
                test3.append(arr[i+x][j])
            test4 = test3[::-1]
            if test3 == test4:

                if len(result) == 0:
                    result = test3
    print('#{} {}'.format(tc, ''.join(result)))

