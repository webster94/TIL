def permutation(s,idx):
    if s == M: # 길이가 곧 깊이군..
        print(' '.join(map(str,arr)))
        return
    for i in range(idx,N): # 내려가게 하는 것을 막기위해 포문 시작을 여기서 Idx에서 했다.
        arr.append(i+1)   #  넣고시작
        permutation(s+1,i)  # 깊이!
        arr.pop()# 나오면 끝에 숫자 제거 하고 다음 포문 진행

N,M = map(int,input().split())
arr= []
visited= [0] *N
permutation(0,0)