T = int(input())
for tc in range(1, T+1):
    a = input()
    b = input()
    la = len(a)
    lb = len(b)
    
    result = 0
    for j in range(lb-la+1):
        for i in range(la):
            if a[0:la] == b[j:j+la]:
                result = 1
    print('#{} {}'.format(tc, result))