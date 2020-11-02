import sys
sys.stdin = open('이진수2.txt','r')
T = int(input())
for t in range(1,T+1):
    N = float(input())
    result = ''
    n = 1
    while N > 0 :
        if  N > 0 and N >= (1 /(2 ** n)):
            N = N - (1 / (2 ** n))
            result += '1'
        elif 0 < N <  (1 /(2 ** n)):
            result += '0'

        else:
            result += '0'
        if N == 0:
            break
        n+=1
    if len(result) < 12:
        print("#{} {}".format(t,result))
    else:
        print("#{} overflow".format(t))
