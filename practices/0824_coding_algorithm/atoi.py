
def atoi(string1):
    result = []
    result1 = 0
    for i in string1:
        result.append(ord(i)-48)
    for j in range(len(result)):
        result1 += result[j]*10**(len(result)-1-j)
    return result1



string1 = atoi('1234')
print(type(string1),string1)

def atoi(line):
    num = 0

    for i in range(len(line)):
        num *= 10
        num += ord(line[i])-ord('0')
    return num
num = atoi('1234')
print(type(num),num)


def itoa(num):
    line = ''
    tmp = num
    while tmp >0:
        number = tmp%10
        line +=chr(number+ ord('0'))
        tmp //= 10
    line = line[::-1]
    return line
line = itoa(1234)
print(type(line), line)