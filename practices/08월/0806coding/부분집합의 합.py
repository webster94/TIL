# 1부터 12
# n = 이 원소의 개수
# k = 원소의 합인 원소의 개수를 출력해야한다.
# 집합이 없는 경우 0 출력
# 테스트 케이스 개수
# 1. t, n k 받는다
# 부분집합을 출력
# 원소의 개수가 n개고 합이 k 가 되는 부분집합의 개수를 출력
A = [1,2,3,4,5,6,7,8,9,10,11,12]
T = int(input())
for t in range(1,T+1):
    N,K = list(map(int,input().split()))
    result = 0
    for i in range(1<<12):
        total = 0
        count = 0
        for j in range(13):
            if i & (1<<j):
                total += A[j]
                count += 1
        if count == N and total == K:
            result +=1
    print(f'#{t} {result}')