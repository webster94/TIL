
import sys
sys.stdin = open("sample_input.txt", "r")


T = int(input())                # 테스트 케이스 수 입력

for tc in range(1, T+1):

    str1 = list(str(input()))   # 문자열1 입력
    str2 = list(str(input()))   # 문자열2 입력
    i = 0                       # str1 인덱스 시작점 i 설정
    j = 0                       # str2 인덱스 시작점 j 설정
    M = len(str1)
    N = len(str2)
    cnt = 0                      # 숫자 카운팅 변수 초기화

    while i<M and  j<N:           # 길이를 벗어나지 않는 범위 내에서 탐색
        for i in range(1, M):
                for j in range(1, N): # str1 안의 글자들 순차적으로 탐색
                    if str1[i] == str2[j]:   # 같은 글자 발견하면
                        cnt += 1            # 카운팅 + 1
                    else:                   # 같은 글자 없으면
                        cnt = 0             # 0 출력
                break                            # 범위 설정이 되어 있으므로 i, j +=1은 하지 않는다.

 print('#{} {}'.format(tc, cnt))





