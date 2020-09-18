import sys
sys.stdin = open("input2.txt","r")

for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    real = ''

    myList = [list(input()) for _ in range(N)]



    for i in range(N-M+1):
        for j in range(N):
            str1 = ''
            str2 = ''
            str3 = ''
            str4 = ''
            for r in range(M):
                str1 += myList[i + r][j]
                str2 += myList[i + M -r - 1][j]

                str3 += myList[j][i + r]
                str4 += myList[j][i + M - r - 1]
            if str1 == str2:
                real = str1
                break
            if str3 == str4:
                real = str3
                break

        if real != '':
            break


    print(f'#{T} {real}')