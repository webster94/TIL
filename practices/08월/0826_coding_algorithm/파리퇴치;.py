T = int(input())
for t in range(1,T+1):
    # 먼저 파리부터 입력을 받자.
    N , M = map(int,input().split())
    flies = []
    for i in range(N):
        flies.append(list(map(int,input().split())))
    # 파리가 이제 채에 올라왔다. 잡으러가야지!
    killed = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for k in range(M):
                total += sum(flies[i+k][j:j+M])
            killed.append(total)
    print(max(killed))