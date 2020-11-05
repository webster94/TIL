# 정렬시키고
# 반쪽 갈라서
# 인덱스 조정
# 근데 어떻게 반 나눈것도 확인하지?????

T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = list(map(int,input().split()))
    ans = 0
    for key in B:
        l = 0
        r = N - 1
        while l <= r :
            mid = ( l + r ) // 2

            if key == A[mid]:
                ans += 1
                break
            elif key > A[mid]:
                l = mid + 1
                if flag == 1: break
                flag = 1
            else:
                r = mid  - 1
                if flag == -1: break
                flag = -1
    print("#{} {}".format(t,ans))

