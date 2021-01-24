import sys
sys.stdin = open("input.txt", "r")


'''
문자열 두개를 동시에 읽으면서
첫번째 문자열=XYPV
두번째 문자열=EOGGXYPVSY

만약에 첫번째 문자열의 첫번째 값과 같은 글자를 2번 문자열에서 발견한다면?


'''
#1 어제베운 brute force를 이용했다
for test_case in range(1, int(input())+ 1):
    str1=input()
    str2=input()
    A=len(str1)
    B=len(str2)

    for i in range(B-A+1):
        cnt=0
        for j in range(A):
            if str2[i+j]==str1[j]:
                cnt+=1
            else:
                break

        if cnt==A:
            result=1
            break

        else:
            result=0

    print(f'#{test_case} {result}')



