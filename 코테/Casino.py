N,M = map(int,input().split())
cards = list(map(int,input().split()))
cards.sort()
maxtotal = []
maxtotal2 = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            total = 0
            total += cards[i] + cards[j]+cards[k]
            if M  < total :continue
            if total <= M:
                maxtotal.append(total)

print(max(maxtotal))
