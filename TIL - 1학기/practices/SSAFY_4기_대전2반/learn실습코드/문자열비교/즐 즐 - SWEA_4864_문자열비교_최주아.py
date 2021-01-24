import sys
sys.stdin = open("input.txt","r")

for T in range(1, int(input()) + 1):
    str1 = input()
    str2 = input()

    count = 0
    K = 1

    for i in range(0, len(str2) - len(str1) + 1):
        count = 0
        for j in range(len(str1)):
            if str2[i+j] == str1[j]:
                count += 1
            else:
                K = 0
                break
        if count == len(str1):
            K = 1
            break

    print(f'#{T} {K}')
