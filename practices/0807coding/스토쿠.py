
T= int(input())
for t in range(1,T+1):
    arr = [[int(x) for x in map (int, (input().split()))] for _ in range(9)]  @ 2차원 배열 형성


    result = 1 # 트루로 설정하고 규정에 부합하지않는 조건 발생시 끝내자
    for i in range(9): # 행
        hor = set()
        ver = set()  # 중복숫자를 제거해주는 set을 사용
        for j in range(9): # 열
            hor.add(arr[i][j])   # 행 체크
            ver.add(arr[j][i])  # 열 체크
        if len(hor) != 9:  # 행의 길이가 9가 아닐 경우 거짓
            result = 0
            break
        if len(ver) != 9: # 열의 길이가 9가 아닐 경우 거짓
            result = 0
            break

    trg = 0
    for x in range(0,9,3):  # 3개 박스씩 체크하기 위한 범위 (행)
        for y in range(0,9,3):  # 3개 박스씩 체크하기 위한 범위(열)
            rec = set()  #중복 제거를 위한 셋 사용
            for i in range(3):  # 3 칸
                for j in range(3): # 3칸
                    rec.add(arr[x+i][y+j])  # 가로 3 , 세로 3 이동
            if len(rec) != 9:  # 9가 아닐 경우 떙!
                result = 0
                trg = 1  # 1일 경우 브레이크
                break
        if trg:  # trg가 발생될 경우 바로나와라
            break
    print(f'#{t} {result}')


