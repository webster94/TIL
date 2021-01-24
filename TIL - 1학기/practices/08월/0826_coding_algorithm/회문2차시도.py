##채린이버전으로가자
T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    result = []
    # 입력을 받아야지
    garo_lst= []
    for i in range(N):  # 행을 다 인풋으로 받아써
        data = input()
        garo_lst.append(data)  #
    # print(data) 입력값 확인
    # 가로부터 갑시다.
        for i in range(len(data)-M+1):
            if data[i:M+i] == data[i:M+i][::-1]: # 슬라이싱을 해서 표현했군
                result.append(data[i:M+i])

    # 세로 줄 확인
    sero_lst = []
    sero_sub_lst = ''
    for x in range(N):
        for y in garo_lst:
            sero_sub_lst += y[x]
        sero_lst.append(sero_sub_lst)
        sero_sub_1st = ''

    for sero_data in sero_lst:
        for j in range(len(sero_data)-M+1):
            if sero_data[j:j+M] == sero_data[j:j+M][::-1]:
                result.append(sero_data[j:j+M])
    print("#{} {}".format(t,result[0]))



