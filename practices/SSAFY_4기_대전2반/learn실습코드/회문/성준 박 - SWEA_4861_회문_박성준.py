T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    letters = []
    for _ in range(a):
        letters.append(input())
    
    result = 0
    for i in range(a):
        for j in range(a-b+1):
            l = letters[i][j:j+b]
            if l == l[::-1]:
                result = l
                break
        if result == l:
            print('#{} {}'.format(tc, result))
            break

    if result != l:
        for m in range(a):
            for n in range(a-b+1):
                k = ''
                for p in range(b):
                    k += letters[n+p][m]
                if k == k[::-1]:
                    result = k
                    break
            if result == k:
                print('#{} {}'.format(tc, result))
                break 