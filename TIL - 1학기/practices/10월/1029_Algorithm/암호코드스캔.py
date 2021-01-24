import sys
sys.stdin = open('이진코드.txt','r')
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
        idx = len(arr[i]) -1
        while idx >= 55:
            if arr[i][idx] and arr[i-1][idx] == 0 :
                pwd = []
                for _ in range(8):
                    c2 =c3 =c4 = 0

                    while arr[i][idx] == 0 : idx -= 1
                    while arr[i][idx] == 1 : c4, idx = c4 + 1, idx -1 # 1카운트
                    while arr[i][idx] == 0 : c3, idx = c3 + 1 , idx - 1
                    while arr[i][idx] == 1 : c2, idx = c2 + 1, idx - 1

                    MIN = min(c2,c3,c4)
                    pwd.append(pattern[(c2//MIN,c3//MIN,c4//MIN)])
                b = pwd[0] +pwd[2] + pwd[4] + pwd[6]
                a = pwd[1] + pwd[3] + pwd[5] + pwd[7]

                if (a * 3 + b) % 10 == 0:
                    ans += a+b
            idx -= 1
    return ans


T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [[] for _ in range(N)]
    for i in range(N) :
        temp = input()

        for j in range(M):
            arr[i] += hexTobin[temp[j]]
    print('#{} {}'.format(t,find()))
