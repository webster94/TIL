TC = int(input())
for tc in range(1,TC+1):
    N,M = map(int,input().split())
    result = []
    garo_lst = []
    for i in range(N):
        data = input()
        garo_lst.append(data)
        for i in range(len(data)-M+1):
            if data[i:M+i]==data[i:M+i][::-1]:
                result.append(data[i:M+i])

    sero_lst = []
    sero_sub_lst = ''
    for x in range(N):
        for y in garo_lst:
            sero_sub_lst +=y[x]
        sero_lst.append(sero_sub_lst)
        sero_sub_1st = ''

    for sero_data in sero_lst:
        for j in range(len(sero_data)-M+1):
            if sero_data[j:M+j] == sero_data[j:M+j][::-1]:
                result.append(sero_data[j:M+j])
    print("#{} {}".format(tc,result[0]))


