import sys

sys.stdin = open("input.txt", "r")

T = int(input())    # 3흡수기
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    check_arr = [0] * 26
    count_arr = [0] * 26

    for i in str1:
        check_arr[ord(i) - ord('A')] = 1
    for j in str2:
        if check_arr[ord(j) - ord('A')] == 1:
            count_arr[ord(j) - ord('A')] += 1

    print("#{} {}".format(test_case, max(count_arr)))
