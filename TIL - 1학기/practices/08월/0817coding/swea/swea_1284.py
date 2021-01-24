# 첫째줄에 테스트케이스
# 각 테스트 케이스마다  P , Q,R,S,W 순서대로 주어진다/

T = int(input())
for t in range(T + 1):
    P,Q,R,S,W = list(map(int, input().split()))
    A_result = 0
    B_result = 0
    A_result = P*W
    if R>W :
        B_result = Q
    else:
        B_result = Q + (W - R) * S
    if A_result > B_result:
        print(f'#{t} {B_result}')
    else:
        print(f'#{t} {A_result}')
    # 입력 받았다.
    # P a회사 1l당 요금
    # Q 기본 사용량
    # R 월간 사용량
    # S 초과사용량 부과금
    # W 종민의의 수도의 양
