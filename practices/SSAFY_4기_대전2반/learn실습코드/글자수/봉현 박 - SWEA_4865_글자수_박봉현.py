t = int(input())
for tc in range(1, t+1):
    str1 = input()
    str2 = input()
    counts =[]
    for s1 in str1:
        count = 0
        for s2 in str2:
            if s1 == s2:
                count += 1
        counts.append(count)

    print('#{} {}'.format(tc ,max(counts)))

