T = int(input())

def find(long, short):
    i, j = 0, 0
    while j < len(short) and i < len(long):
        if long[i] != short[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j == len(short):
        return 1
    else:
        return 0

for i in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = find(str2, str1)
    print('#{} {}'.format(i, result))