import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input())+ 1):
    str1=input()
    str2=input()
    cnt, sub_cnt=0,0
    #str1, str2를 동시에 읽으면서
    #str1의 원소가 str2에 있다면,
    #몇개가 있는지 세고/그거 어디다가 넣어주고
    #반복하다가, cnt가 더 크면 그걸로 갱신함

    for i in str1:
        #sub_cnt는 중간정산을 하는 변수이다. 따라서 두번째로 x를 다세서 sub_cnt를 넣고
        #그 다음 문자를 또 세줄때는 다시 sub_cnt를 초기화하고, +1을 해줘야한다!
        sub_cnt = 0
        for j in str2:
            if i==j:
                sub_cnt+=1 #x가 몇개인지 세줌,
        if sub_cnt>cnt:
            cnt = sub_cnt

    print(f'#{test_case} {cnt}')





