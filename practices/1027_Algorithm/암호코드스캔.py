pattern = {(2, 1, 1): 0,
           (2, 2, 1): 1,
           (1, 2, 2): 2,
           (4, 1, 1): 3,
           (1, 3, 2): 4,
           (2, 3, 1): 5,
           (1, 1, 4): 6,
           (3, 1, 2): 7,
           (2, 1, 3): 8,
           (1, 1, 2): 9}

hexTobin = {'0': [0, 0, 0, 0], '1': [0, 0, 0, 1], '2': [0, 0, 1, 0], '3': [0, 0, 1, 1], '4': [0, 1, 0, 0],
            '5': [0, 1, 0, 1], '6': [0, 1, 1, 0], '7': [0, 1, 1, 1], '8': [1, 0, 0, 0],
            '9': [1, 0, 0, 1], 'A': [1, 0, 1, 0], 'B': [1, 0, 1, 1], 'C': [1, 1, 0, 0], 'D': [1, 1, 0, 1],
            'E': [1, 1, 1, 0], 'F': [1, 1, 1, 1]}
def find():
    ans = 0
    for i in range(N):
        idx = len(arr[i]) - 1 # 뒤에서 부터 시작
        while idx >= 55:
            # 바로 위행의 값이 없어야 처음만나
            if arr[i][idx] and arr[i - 1][idx] == 0:
                pass


for tc in range(1,int(input()) + 1 ):
    N,M = map(int,input().split())
    arr = [[] for _ in range(N)]

    for i in range(N):
        tmp = input() # 한줄씩 받음
        for j in range(M):
            print(tmp[j])
            arr[i] += hexTobin[tmp[j]]

    # print("#{} {}".format(tc,find()))