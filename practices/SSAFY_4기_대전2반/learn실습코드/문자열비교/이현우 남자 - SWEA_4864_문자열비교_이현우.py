def brute_force(n, m):
    A = len(n)
    B = len(m)
    result = 0
    for i in range(B-A+1):
        cnt = 0
        for j in range(A):
            if n[j] == m[i+j]:
                cnt += 1
            else:
                break
        if cnt == A:
            result = 1
            break
    return result

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    total = brute_force(str1, str2)
    print('#{} {}'.format(tc, total))
