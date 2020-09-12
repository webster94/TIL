# print(type(int("123")))
# str() int()
# "1234" -> 1234
# atoi #문자열을 int형으로 전환
#
# def atoi(line):
#     num = 0
#
#     for i in range(len(line)):
#         num *= 10
#         num += ord(line[i])-ord('0')
#
#     return num
#
# num = atoi("1234")
#
# print(type(num), num)


#
# 1234 -> "1234"
# itoa #인트형을 문자열로 전환
#
#
def itoa(num):
    line = ''
    tmp = num
    while tmp > 0:
        number = tmp % 10
        line += chr(number + ord('0'))
        tmp //= 10

    return line


line = itoa(1234)
# 결과는 뒤집어야 한다.

print(type(line), line)
