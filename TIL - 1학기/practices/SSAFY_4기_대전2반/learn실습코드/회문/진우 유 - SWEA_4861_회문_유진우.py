for c in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [' '.join(input()).split() for _ in range(n)]
    def check(a):
        if len(a) < 2:
            return a
        if a[0] == a[-1]:
            return a[0] + check(a[1:-1]) + a[-1]
        else:
            return ''
    # row
    for row in arr:
        for i in range(n-m+1):
            t = ''.join(row[i:m+1+i])
            if len(check(t))==m:
                result = check(t)
    # col
    for col in zip(*arr):
        col = list(col)
        for i in range(n-m+1):
            t = ''.join(col[i:m+1+i])
            if len(check(t))==m:
                result = check(t)
    print(f'#{c} {result}')