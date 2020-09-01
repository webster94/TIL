import sys; sys.stdin = open("sample_input (5).txt","r")# 입력받고
# 검색 도구를 함수로받자 이때 가로열 ,세로열 한번에
# 비교는 슬라이싱으로!
#회문을 출력하면 break!
def check(li):
    for i in range(N):
        tmp = []
        for j in range(N-M+1):
            if li[i][j:j+M] == li[i][j:j+M][::-1]:
                tmp = li[i][j:j+M]
                return tmp
        for j in range(N-M+1):
            tmp = []
            for k in range(M):
                tmp.append(li[j+k][i])
            if tmp == tmp[::-1]:
                return tmp
    return []


T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [input() for _ in range(N)]
# 입력 받음
    ans = check(arr)
    print("#{} {}".format(t,''.join(ans)))