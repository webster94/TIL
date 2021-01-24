import sys
sys.stdin = open("input (26).txt","r")
def check(x,y):
    if x < 0 or x >= 100 or y< 0 or y >= 100: return False
    if arr[x][y] == 0: return False
    return True



for tc in range(1,11):
    case_num = input()
    arr = [list(map(int,input().split())) for _ in range(100)]
    '123456'
    x= y = 0 # 도착점 찾기
    for i in range(100):
        if arr[99][i] == 2:
            x,y = 99,i
            break  #
    dir = 0  #방향 정보
    while x:
        #  왼쪽으로 가는 경우
        if dir != 2 and check(x,y-1):
            y -= 1 ; dir = 1 # 방향정보를 저장해줘야함
        elif dir != 1 and check(x,y+1): # 오른쪽으로 가는 경우
            y += 1 ; dir = 2
        else: # 그 외, 위로 가는 경우
            x -= 1; dir = 0
        # 오른쪽으로 가는 경우
    print(y)