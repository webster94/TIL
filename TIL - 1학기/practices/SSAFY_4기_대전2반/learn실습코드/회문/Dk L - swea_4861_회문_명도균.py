def pal_test(arr):
    result = []
    for a in arr:
        for i in range(N-M+1):
            if a[i:i+M] == a[i:i+M][::-1]:
                result = a[i:i+M]
                break
    return result

def v_test(arr):
    vertical = []
    for x in range(N):
        v = ''
        for y in range(N):
             v += arr[y][x]
        vertical.append(v)
    return vertical

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    words = [input() for _ in range(N)]
    result = pal_test(words)
    
    if bool(result) is True:
        print('#{} {}'.format(test_case, result))
    else:
        vertical = v_test(words)
        result = pal_test(vertical)
        print('#{} {}'.format(test_case, result))

                         