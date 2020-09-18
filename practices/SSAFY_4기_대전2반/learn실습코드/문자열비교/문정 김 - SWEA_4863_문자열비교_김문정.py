T = int(input())
for tc in range(1, T+1):
    str1 = input() #p
    str2 = input() #t
    li_1 = list(str1)
    li_2 = list(str2)
    i, j = 0, 0
    while i < len(str2) and j < len(str1):
        if li_1[j] != li_2[i]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == len(str1):
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))
