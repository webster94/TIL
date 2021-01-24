# # #for else 구문
# # for i in range(1, 11):
# #     if i == 15:
# #         break
# # else:
# #     print("중간에 멈추지 않음 ")
#
def check(str1, str2):
    #본문에서 패턴길이를 빼고 +1 하여 반복
    for i in range(len(str2) - len(str1) + 1):
        #패턴의 길이만큼
        for j in range(len(str1)):
            #만약 현재사이클에 다르다면 브레이크
            if str2[i + j] != str1[j]:
                break
        #중간에 브레이크 걸리지 않았다면 완벽히 찾은것
        else:
            return 1
    #완벽히 찾지 못했다면 리턴 0
    return 0


T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    print("#{} {}".format(tc, check(str1, str2)))

    # in 활용하여 체크
    # if str1 in str2:
    #     print("#{} {}".format(tc, 1))
    # else:
    #     print("#{} {}".format(tc, 0))

    # ans = 0
    # if str2.find(str1) != -1:
    #     ans = 1
    # print("#{} {}".format(tc, ans))


#find함수 사용법
# str1 = "1235"
#
# str2 = "111234"
#
# print(str2.find(str1))