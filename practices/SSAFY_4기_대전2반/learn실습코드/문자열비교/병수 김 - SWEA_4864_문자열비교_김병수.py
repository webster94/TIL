T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    i = 0
    j = 0

    while i < len(str1) and j < len(str2):
        if str1[j] != str2[i]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == len(str1):
            print('#{} {}'.format(tc,1))

    else:
        print('#{} {}'.format(tc,0))
