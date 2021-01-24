import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    str1 = input()  # 짧은거
    str2 = input()  # 긴거
    result = 0
    for i in range(len(str2) - len(str1)+1):
        cnt = 0
        for j in range(len(str1)):
            if str2[i+j] == str1[j]:
                cnt += 1
            else:
                break
        if cnt == len(str1):
            result = 1
    print('#{} {}'.format(test_case, result))






