str1 = "A pattern matching algorithm"
str2 = "ritfhm"

def 고지식패턴(str1, str2):
    A = len(str1)
    B = len(str2)

    for i in range(A-B+1):
        cnt = 0
        for j in range(B):
            if str1[i+j] == str2[j]:
                cnt += 1
            else:
                break

        if cnt == B:
            return i

    return -1

tmp = 고지식패턴(str1, str2)

print(tmp)


