def sol(n):
    v.append(n);r=0
    for i in board[n]:
        if i not in v:
            if i==g:return 1
            elif r==0:r+=sol(i)
    return r
for t in range(int(input())):
    v,e=map(int, input().split());board=[[] for _ in range(v+1)];v=[];r=0
    for _ in range(e):s,f=map(int,input().split());board[s].append(f)
    s,g=map(int,input().split());print(f'#{t+1}',sol(s))