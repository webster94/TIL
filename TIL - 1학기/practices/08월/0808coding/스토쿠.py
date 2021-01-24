T = int(input())
for t in range(1,T+1):
    matrix = [[int(x) for x in list(map(int, input().split()))] for _ in range(9)]
    testcase = [[0]*10 for _ in range(10)]
    result = 1
    # 0이 되면 바로 브레이크!
    # 가로 횡 확인 후에 3*3 확인하자
    for i in range(9):
        garo = set()
        sero = set()
        for j in range(9):
            garo.add(matrix[i][j])
            sero.add(matrix[j][i])
        if len(garo) !=9:
            result =0
            break
        if len(sero) !=9:
            result =0
            break
    cnt = 0
    for a in range(0,9,3):
        for b in range(0,9,3):
            che = set()
            for k in range(3):
                for m in range(3):
                    che.add(matrix[a+k][b+m])
            if len(che) !=9:
                result = 0
                cnt =1
                break
    print(f'#{t} {result}')
