import sys
sys.stdin = open("스도쿠.txt","r")
T = int(input())
for t in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    flag1 = True
    flag2 = True
    for i in range(9):
        sero = set()
        garo = set()
        for j in range(9):
            garo.add(arr[i][j])
            sero.add(arr[j][i])
        if len(garo) != 9 or len(sero) != 9:
            flag1 = False
            break
    for i in range(0,9,3):
        for j in range(0,9,3):
            mgaro = set()
            msero = set()
            for n in range(3):
                for m in range(3):
                    mgaro.add(arr[i+n][j+m])
            if len(mgaro) != 9:
                flag2 = False
    if flag2 == False or flag1 == False :
        print("#{} 0".format(t))
    else:
        print("#{} 1".format(t))