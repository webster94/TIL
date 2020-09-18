# 테스트 입력받아
# n,m입력을 받고
# 2차원 배열 입력을 포문을 이용해서 받자.
# 가로를 체크하자
# 체크하는 방법? 슬라이싱을 활용하자
# 세로를 체크 하자
# 세로를 체크하는 방법은 세로를 뽑아서 따로 서브에 저장하고
# 서브를 가로처럼 확인 한 후
# result에 넣어서 보내자!

T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split()) # n열의 길이와 회문 m줄
    result = []
    arr = []
    for i in range(N):
        data = input()
        arr.append(data)  # arr 에 정보들어온 것 확인
    # 가로체크
        for i in range(len(data)-M+1):
            if data[i:i+M] == data[i:i+M][::-1]: # ㅁㅊ 1차원 데이터그대로였꾸나
                result.append(data[i:i+M]) # 그래서 포문을 한게 썻군..
    # 세로 체크
    #세로 체크에 필요한 것은 빈 문자열 변수와 빈 리스트 하나!
    sero = []
    sero_sub = ''
    # 세로열을 쫙 가지고오자
    for x in range(N): # 열의 갯수
        for y in arr: # 각 행이 가지고 잇는 정보
            sero_sub += y[x]
        sero.append(sero_sub)
        sero_sub = ''
    # 오키 가져온것 확인 근데 문자열임 2차원으로 만들어줘야함
    # 만들어줬음!
    #이제 다시 세로열에서 회문이 있는지 확인하자
    for sero_data in sero:
        for i in range(len(sero_data)-M+1):
            if sero[i:i+M] == sero[i:i+M][::-1]:
                result.append(sero[i:i+M])

    print("#{} {}".format(t,result))



