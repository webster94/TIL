T = int(input())

def pal_check(line):
    for idx in range(len(line) // 2):
        if line[idx] != line[-idx - 1]:
            return False
    return True

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    found = False
    arr = [list(input()) for _ in range(N)]
    print('#{}'.format(tc), end = " ")
    for i in range(N):
        for j in range(N - M + 1):
            sample = arr[i][j:j + M]                # 가로
            sample2 = [a[i] for a in arr[j:j + M]]  # 세로
            if pal_check(sample):
                print(''.join(sample))
                found = True
                break
            elif pal_check(sample2):
                found = True
                print(''.join(sample2))
        if found:
            break