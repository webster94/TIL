T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    res = {}

    for i in str1:
        res[i] = str2.count(i)

    print('#{} {}'.format(tc, max(res.values())))
