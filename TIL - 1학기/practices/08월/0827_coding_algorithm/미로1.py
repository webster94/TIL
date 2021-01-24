# 입력

for t in range(1,11):
    tc_1 = int(input())
    tc = [[int(x) for x in input().split()] for _ in range(10)]


    dr = [0,1,0,-1]
    dc = [1,0,1,0]
    d= 0 # 0 : 하 1: 우 , 2: 하 , 3: 좌
    # r = 0
    # c = 0
    # num = 1
    #
    # for i in range(100):
    #     if tc[0][i] == 1:
    #         # 시작
    #         while True:
    #             tc[r][c] = num
    #             num +=1
    #
    #             cr = r+

