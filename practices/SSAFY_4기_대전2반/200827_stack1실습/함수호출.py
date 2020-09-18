# 1부터 N 까지 더하는 프로그램을 만들고 싶다.


# total = 0
#
# for i in range(1, 10+1):
#     total += i
# print(total)
#
# total2 = 0
# for i in range(1, 101):
#     total2+= i
#
# print(total2)


def mySum(N):
    tmp = 0
    for i in range(1, N + 1):
        tmp += i

    return tmp


# print(mySum(10))
# print(mySum(100))


def mySum2(N):
    global total3

    for i in range(1, N + 1):
        total3 += i


total3 = 0

mySum2(100)


#
# print(total3)


# 3
# 100
# 1000
# 10000

# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#
#     print(mySum(N))

# None 출력해보기
def check(N):
    if N % 2 == 0:
        return
    else:
        return 1


print(check(1))
print(check(2))
