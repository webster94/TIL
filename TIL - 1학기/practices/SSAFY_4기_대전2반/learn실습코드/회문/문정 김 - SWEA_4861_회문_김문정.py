# T = int(input())
# for tc in range(1, T+1):
# # 2차원 리스트 입력
# # 한 행씩 읽어가며 처음 == 끝 확인
# # 같으면, res에 추가 , res 길이 == 회문의 절반길이 이면 빠져나오기
# # 행을 다 돌아도 길이를 만족하는 res 없을 경우, 열 비교
#     N, M = map(int, input().split()) #N은 글자길이 M은 회문길이
#     arr = [list(input()) for _ in range(N)]
#     res = []
#     L = len(res)
#     # 가로 회문
#     while L != int(M/2):
#         for i in range(N):
#             res = [] #행이 바뀌면 res 초기화
#             for j in range(int(N/2)):
#                 if arr[i][j] == arr[i][M-1-j]: #처음이랑 끝이랑 같으면
#                     res.append(arr[i][j]) # 여기서 길이를 만족해도 while을 빠져나오지 않아요
#                     L = len(res)
#                     #print(int(M/2)==L True로 나와요
#                 else:
#                     continue
#         if i == (N-1): # for문 다 돌았지만 회문을 찾지 못한 경우
#             break
#
#     if len(res) != int(M/2):
#     #세로 회문
#         for j in range(N):
#             res = []
#             for i in range(int(N/2)):
#                 if arr[i][j] == arr[N-1-i][j]: #처음이랑 끝이랑 같으면
#                     res.append(arr[i][j])
#                 else:
#                     continue
#                 if len(res) == M:  # 회문이 완성되면 중간에 나오기
#                     break
#             print(res)
#
#     print('#{} {}'.format(tc, ''.join(res)))

# import sys
# sys.stdin = open()
T = int(input())

def test(texts): # 회문을 판별하는 함수
    if texts == texts[::-1]:
        return texts

def transpose(array): # 행과 열을 바꿔주는 함수
    row = len(array) # 행
    col = len(array[0]) # 열
    array_T = [[0 for _ in range(row)] for _ in range(col)] # 전치함수를 넣을 배열
    for i in range(row):
        for j in range(col):
            array_T[i][j] = array[j][i] # 전치
    return array_T

for tc in range(1, T+1):
    N, M = map(int, input().split()) #N은 글자길이 M은 회문길이
    arr = [list(input()) for _ in range(N)]
    arr_T = transpose(arr)

    for i in range(N):
        for j in range(N-M+1):#arr의 시작점은 0부터 N-M까지,
            samples = arr[i][j:j+M] #i행에서 j부터 j+M-1까지 슬라이싱, end를 포함하지 않는다.
            samples_T = arr_T[i][j:j + M]
            if test(samples): # 행에서 회문찾아서 있으면 출력
                print('#{} {}'.format(tc, ''.join(samples)))
            else:                   # 행에서 못찾으면
                if test(samples_T): # 열에서 찾아서 출력 (전치했으니 열이 행됐다.)
                    print('#{} {}'.format(tc, ''.join(samples_T)))