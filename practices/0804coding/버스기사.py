#충전소를 확인한다.
# k 칸 안에 충전소가 있으면 최대한 큰 값으로 이동한다, cnt +1
# 충전소를 확인한다, 다시 이동한다!
# 10칸 이동하면 끝!

# 길 배열 선언
# 반복문, 변수 초기화
# for 문으로 충전기 찾기
# 충전기 찾으면 이동, 충전 횟수 추가
# 종점 도착시 만족시 종료
T =int(input())
for t in range(1,T+1):
    k,n,m = list(map(int,input().split()))
     ## 정류장 리스트
    chargers = list(map(int,input().split()))
    road = [0 for x in range(0,n+1)] # 길에 충전소 넣음  ## 암기
    for char in chargers:
        road[char] = 1    ## 충전소를 road 값에 넣는다!
    cnt = 0
    mypo = 0
    can_out = False     #  변수에 false를 잡고 있으니까!!
    while True:
        next = -50    # 다음 확인창 종료조건, 다음위치 , 갈때가 없다 그럼 -50인 상태로 종료
        for i in range(mypo+1,mypo+k+1):  # 내 앞부터 k까지 확인
            if road[i] ==1:   # 충전소가 잇다!
                next = i  # 다음위치를 i로 옮긴다
            if i>=n:   # 종료조건! i가 n보다 크면 종료
                can_out= True    # true로 바꾸고 브레이크로 for 문을 나간다, while문은 나가지지않는다.
                break
        if can_out:  #while 문 나가는 것
            break
        if next == -50:  # 움직일 곳이 없는 경우 나가는 것
            cnt = 0
            break
        mypo = next
        cnt += 1

    print(f'#{t} {cnt}')


