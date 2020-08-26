TC = int(input())
for tc in range(1, TC + 1):  # case를 받고,
    N, M = map(int, input().split())  # n,m을 각각 받는다
    result = []  # 펠린드롬을 받을 result

    # 가로줄 확인
    Garo_lst = []  # 1 가로 빈리스트에 data를 넣는다
    for i in range(N):  # 2
        Data = input()
        Garo_lst.append(Data)  #행이었구나
        for i in range(len(Data) - M + 1):  # 4 가로줄 체크!
            if Data[i:M + i] == Data[i:M + i][::-1]:  # 5  거꾸로 나열도 해주네?
                result.append(Data[i:M + i])

    # 세로줄 확인
    Sero_lst = []  # 6
    Sero_sub_lst = ''  # 7
    for x in range(N):  # 8  열
        for y in Garo_lst:  # 9 행
            Sero_sub_lst += y[x]  # 10  행의 열들 나열
        Sero_lst.append(Sero_sub_lst)  # 11
        Sero_sub_lst = ''  # 12


    for sero_data in Sero_lst:
        for j in range(len(sero_data) - M + 1):
            if sero_data[j:M + j] == sero_data[j:M + j][::-1]:
                result.append(sero_data[j:M + j])

    # print(result)
    print("#%d %s" % (tc, result[0]))  # 13