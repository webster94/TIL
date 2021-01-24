# 총 이동거리 계산
T = int(input())
for t in range(1,T+1):
    number = int(input())
    # 변화량을 이용
    distance = 0
    vel = 0
    for num in range(0,number):
        test = list(map(int, input().split()))
        if test[0] == 1:
            vel += test[1]
        elif test[0] == 2:
            if vel>test[1]:
                vel -= test[1]
            else:
                vel = 0
        distance += vel
    print(f'#{t} {distance}')


