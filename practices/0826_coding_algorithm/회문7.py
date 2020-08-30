T= int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    result = []
    garo = []
    for i in range(N):
        data = input()
        garo.append(data)
        for i in range(N-M+1):
            if data[ i : i + M] == data[i :i + M][::-1]:
                result.append(data[i : i + M])

    sero = []
    sero_sub = ''
    for x in range(N):
        for y in garo:
            sero_sub += y[x]
        sero.append(sero_sub)
        sero_sub = ''
    print(sero)

    for sero_data in sero:
        for j in range(len(sero_data)-M+1):
            if sero_data[j : j+M] == sero_data[j : j + M][::-1]:
                result.append(sero.data[j : j + M])
    print("#{} {}".format(t, result))

