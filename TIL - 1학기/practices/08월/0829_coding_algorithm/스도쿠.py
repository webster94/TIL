import sys; sys.stdin = open("스도쿠.txt","r")# 입력을 받는다.
# 2차원배열에 스도쿠를 입력시킨다.
# 2중포문으로 검사하고, set에 저장해서 길이를 확인한다.
# 확인이 1 길이가 9이 아니면 0을 출력후 break 한다.
T = int(input())
for t in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    # 입력 받았음
    # 이제 확인해야지
    result = 1
    # set 확인함
   #가로열
    for i in range(9):
        check = set()
        for j in range(9):
            check.add(arr[i][j])
        if len(check) != 9:
            result = 0
            break
    # 세로 체크
        check2 = set()
        for j in range(9):
            check2.add(arr[j][i])
        if len(check2) != 9:
            result = 0
            break

    #3X3 박스는 쉽다
    for i in range(0,9,3):
        for j in range(0,9,3):
            check3 = set()
            for n in range(3):
                for m in range(3):
                    check3.add(arr[i+n][j+m])
            if len(check3) != 9:
                result = 0
                break
    print("#{} {}".format(t,result))



