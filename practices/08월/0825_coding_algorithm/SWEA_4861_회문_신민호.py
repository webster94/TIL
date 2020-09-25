def examine(line):
    for i in range(len(line)//2):
        if line[i] != line[-i-1]:
            return False
    return True  # 검사기 만듬

T = int(input())
for t in range(1,T+1):
    N,M = map(int,(input().split()))
    found = False
    arr = [list(input()) for _ in range(N)]
    print('#{}'.format(t),end =" ")
    for i in range(N):
        for j in range(N-M+1):
            sample = arr[i][j:j+M]
            sample2 = [a[i] for a in arr[j:j+M]]
            if examine(sample):
                print(''.join(sample))
                found = True
                break
            elif examine(sample2):
                found = True
                print(''.join(sample2)
        if found:
            brea