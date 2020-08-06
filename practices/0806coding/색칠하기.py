# 빈리스트를 만든다.
# for 루프를 넣어서 숫자값을 넣는다. 빨간색, 파란색 나눠서! 빨간색 1, 파란색 2
# 겹치는 부분은 3이 된다!!

T = int(input())
for t in range(1,T+1):
    crt = int(input())
    large = []
    # for c in range(crt):# 색칠영역
    #li = [[int(x) for x in input().split()] for _ in range(crt)] #2차원 배열 생성
    matrix = [[0]*10 for _ in range(10)]
    total = 0
    # 입력값을 활용
    li = [[int(x) for x in input().split()] for _ in range(crt)]
    for n in range(crt):
        xx1 = li[n][0]
        yy1 = li[n][1]
        xx2 = li[n][2]
        yy2 = li[n][3]
        count = li[n][4]
        for i in range(xx1,xx2+1):
            for j in range(yy1,yy2+1):
                matrix[i][j] += 1
    for i in matrix:
        total +=(i.count(2))
    print(total)



    # matrix = [[0 for _ in range(10)] for j in range(10)]
    # for n in range(crt):
    #     xx1= li[n][0]
    #     yy1= li[n][1]
    #     xx2= li[n][2]
    #     yy2= li[n][3]
    #     color=li[n][4]
        #  이중포문!
        # print(f'(x1,y1)=({xx1}.{yy1})//(x2,y2)=({xx2}.{yy2})//color={color}')
        # for j in li:
        #     print(li[i][j])
    #    li = [[int(x) for x in input().split()] for _ in range(100)]
    # 배열을 받았고 이제 빈배열을 만들자.
    # matrix = [[0 for i in range(10)] for j in range(10)]
    # # 색깔을 입힌다.
    #     #for  cor in color:   # 선언에서 문제, 1,2, 인지 확인
    # if info[4] == 1:
    #     maxtrix[info[0]]~ [info[2]] = 1