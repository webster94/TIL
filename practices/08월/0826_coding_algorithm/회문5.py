# # 다시..
# 입력을 받는다 . 테스트, (N,M), 그리고 data
# 가로는 한번에 확인해보자
# 세로는 데이터를 다시 받아서 가로처럼 비교를 하자
# 이때 포문을 잘 써야한다.
T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    result = []
    garo_list = []
    for i in range(N):
        data = input()
        garo_list.append(data)
        for i in range(len(data)-M+1):
            if data[i:i+M] == data[i:i+M][::-1]:
                result.append(data[i:i+M])
        # 가로 확인
#세로 확인가자
# 세로를 보는 것은 어렵다 세로열만 따로 모아서 가자
    sero = []
    sub = ''
    for i in range(N):
        for j in garo_list:
            sub += j[i]
        sero.append(sub)
        sub = ''
    # print(sero) # 세로열만 따로 저장한거 확인
    for i in sero:
        for j in range(len(i)-M+1):
            if i[j:j+M] == i[j:j+M][::-1]:
                result.append(i[j:j+M])
                print(result)

    print('#{} {}'.format(t,result))
