# 체크 배열, 카운트배열

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    check_arr = [0] * 26
    count_arr = [0] * 26

    # 1. str1을 순회하면서 알파벳 체크
    for i in str1:
        check_arr[ord(i) - ord('A')] = 1
    # 2. 체크된 알파벳의 카운트 세기
    for i in str2:
        if check_arr[ord(i) - 65] == 1:
            count_arr[ord(i) - 65] += 1

    print("#{} {}".format(tc, max(count_arr)))

#파이썬 필살기 느낌
    # dict = {}
    # for i in str1:
    #     if i not in dict:
    #         dict[i] = str2.count(i)
    # print("#{} {}".format(tc, max(dict.values())))
