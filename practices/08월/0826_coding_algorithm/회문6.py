T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    garo_list = []
    result = []
    for i in range(N):
        data = input()
        garo_list.append(data)
        for i in range(len(data)-M+1):
            if data[i:i+M] == data[i:i+M][::-1]:
                result.append(data[i:i+M])
    # 세로를 따로 입력해놓자
    sero = []
    sub = ''
    for i in range(N):
        for j in garo_list:
            sub += j[i]
        sero.append(sub)
        sub = ''
#    세로 배열 완료
    for sero_data in sero:
        for j in range(len(sero_data)-M+1):
            if sero_data[j:j+M] == sero_data[j:j+M][::-1]:
                result.append(sero_data[j:j+M])
    print("#{} {}".format(t,result[0]))

