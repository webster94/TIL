# 위에 연결이 되는 n_queen이 있는지 확인하면서
N = int(input()) ## 8
cols = [i for i in range(N)]  # 여왕의 자리를 정해놓는다. 0번여왕 0 , 1번여왕 1''' N-1번 여왕 N-1
ans = 0
def nQueen(k): ## 0 ## 1 ## 2 -- ## 8
    global  ans
    if k == N:
        for i in range(N-1):  # 0부터 6까지 실행
            for j in range(i+1,N):   # 1부터 6까지 실행
                if j - i == abs(cols[j] - cols[i]): return
                # 1-0 == 절대값 cols[1] - cols[0] 같네 return!
        ans +=1
    else:
        for i in range(k,N):  # 0부터 7까지 실행 ## 1,7까지 실행
            cols[k],cols[i] = cols[i],cols[k]
            #cols[0]과 cols[0] 을 바꾸고 실행
            # cols[1]과 cols[1] 을 바꾼다
            # cols[2] 와 cols[2]를 바꾼다

            # cols 7까지 동일

            nQueen(k+1) # k = 1 ## k = 2# k = 8
            cols[k], cols[i] = cols[i], cols[k]
            # 다시 바꿔놓고 i는 2
nQueen(0) # 0부터 시작
print(ans)