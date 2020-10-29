import sys
sys.stdin = open('이진수.txt','r')

def calculate(n):
    number = ''
    for i in range(3,-1,-1):
        if n & (1 << i):
            number += '1'
        else:
            number += '0'

    return number

T = int(input())
for t in range(1,T+1):
    N,numberhex = input().split()
    temp = ''
    for i in numberhex:
        result = int(i,16)
        temp += calculate(result)
    print("#{} {}".format(t,temp))

#
# #
#
# a = '010101'
# print(int(a, 2))