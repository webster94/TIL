

T = int(input())

for i in range(1, N+1):
    N, M = map(int, input().split())
    texts = list[]

    pal_arr = [[0 for col in range(N)] for row in range(N)]   :     #여기부터 N*N 크기의 행렬을 만들고 M 글자의 회문글자를 찾아야 함.
    pal_text = list(input())                                        #찾아야 하는 회문글자를 pal_text라고 두고
                                                                    #pal_text에 M개의 글자를 리스트로 받아온다고 가정한다.
    x = 0                                                           # 인덱스 초기 설정, X = 가로
    y = 0                                                           # Y = 세로

    if x[0] == x[M-1]:                                              # 찾아야 하는 회문글자(pal_text)의 [0] [M-1], [1], [m-2] 등등을 비교한다.
                                                                    # 찾았으면 pal_text에 넣어주고, 출력한다.

