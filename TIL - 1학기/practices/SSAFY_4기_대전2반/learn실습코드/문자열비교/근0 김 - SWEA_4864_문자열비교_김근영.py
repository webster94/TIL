import sys
sys.stdin = open("sample_input.txt", "r")


def BTF(str1, str2):
    i = 0
    j = 0
    N = len(str1)
    M = len(str2)

    while i < N and j < M :
        if str2[j] != str1[i] :
            i = -1
            j = j- i
        i += 1
        j += 1
    if i == N:
        return  1
    else:
        return  0


T = int(input())

for tc in range(1, T+1):
    str1 = str(input())
    str2 = str(input())
    print("#{} {}" .format(tc, BTF(str1, str2)))
