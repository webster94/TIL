T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())

    num_list = []
    for char1 in str1:
        cnt = 0
        for char2 in str2:
            if char2 == char1:
                cnt += 1
        num_list += [cnt]

    print("#{} {}".format(tc, max(num_list)))