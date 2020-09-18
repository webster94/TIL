def check(n):
    if n > 2:
        return check(n) = check(n-1) + (2 * check(n-2))
    if n == 2:
        return 3
    else:
        return n


for tc in range(1, int(input())+1):
    N = int(input())
    case = N // 10
    result = check(case)
    print('#{} {}'.format(tc, result))