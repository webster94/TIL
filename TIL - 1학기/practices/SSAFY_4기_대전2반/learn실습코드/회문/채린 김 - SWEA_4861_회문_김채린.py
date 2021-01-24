import sys
sys.stdin = open("input.txt", "r")

'''
회문
문제좀 똑바로 읽자 
N*N행렬에서 M길이짜리 펠린드롬을 찾는것임
'''

#가로줄을 확인할거야
#우선 가로줄로 먼저 받고, 그 각각 요소를 슬라이싱해서 같은지 확인한다.

for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    result=[]

    #가로줄 체크
    garo = [input() for _ in range(n)]
    for ga in garo:
        for j in range(n-m+1):
            if ga[j:j+m] == ga[j:j+m][::-1]:
                result.append(ga[j:j+m])

    #세로줄 체크
    #먼저 sero를 만들어야한다
    sero = []
    sero_sub =''
    for i in range(n):
        for ga in garo:
            sero_sub += ga[i]
        sero.append(sero_sub)
        sero_sub = ''
    #print(sero)

    #세로줄 체크
    for se in sero:
        for j in range(n-m+1):
            if se[j:j+m] == se[j:j+m][::-1]:
                result.append(se[j:j+m])
    #print(f'#{tc} {result[0]}')
    print('#{} {}'.format(tc, result[0]))