T = int(input())
for t in range(1,T+1):
    arr = [[int(x) for x in map(int,input().split())] for _ in range(9)]
    # input값을 받았다
    result = 1
    # 횡체크 열체크
    for i in range(9):
        box1 = set()
        box2 = set()
        for j in range(9):
            box1.add(arr[i][j])
            box2.add(arr[j][i])
        if len(box1) != 9:
            result = 0
        if len(box2) != 9:
            result = 0
            break

# 3*3 박스
    ctr = 0
    for i in range(0,9,3):
        for j in range(0,9,3):
            box3 = set()
            for a in range(3):
                for b in range(3):
                    box3.add(arr[i+a][j+b])
            if len(box3) != 9:
                result = 0
                ctr = 1
                break
        if ctr:
            break

    print(f'#{t} {result}')
