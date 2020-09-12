T = int(input())
for tc in range(1, T+1):
    str1 = str(set(input())) #입력에서 중복문자 없애기
    str2 = input()
    dic = {}
    max_cnt = 0

    # dictionary 만들기
    for s in str1:
        dic[s] = 0
    # count
    for chr in str1:
        for chr2 in str2:
            if chr == chr2:
                dic[chr] += 1
    # max 출력
    for chr in str1:
        if max_cnt < dic[chr]:
            max_cnt = dic[chr]
    print('#{} {}'.format(tc, max_cnt))