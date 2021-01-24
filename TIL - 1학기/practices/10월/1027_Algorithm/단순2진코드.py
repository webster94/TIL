import sys
sys.stdin = open('단순이진코드.txt','r')
info = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    for i in range(N):
        code_1 = input()
        for j in range(M-1,-1,-1):
            if code_1[j] == '1':
                r_code = code_1[j-55:j+1]
                break
        # 7개로 자른 후에 비교를 한다!
    n = []
    for k in range(0,56,7):
            num = info.index(r_code[k:k+7])
            n.append(num)
    odd = 0
    even = 0

    for i,v in enumerate(n):
        if i %2 == 0:
            odd += (v * 3)
        else:
            even += v
    if (odd + even) % 10 == 0:
        print('#{} {}'.format(t,sum(n)))
    else:
        print('#{} 0'.format(t))



