T = int(input())
for t in range(1,T+1):
    sentence = input()
    for n in range(1,15): # 최소 두마디부터 최대 30문자열!
        if sentence[:n] == sentence[n:n*2]:
            print(f'#{t} {n}')
            break
