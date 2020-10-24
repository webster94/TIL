import sys
sys.stdin = open('숨바꼭질.txt','r')
from collections import deque
def bfs(dist,n,k):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x ==k:
            return dist[x]
        for i in (x+1,x-1,2*x):
            if 0<= i <= 100000 and dist[i] == 0 :
                dist[i] = dist[x] + 1 # count 역할
                q.append(i)

N,K = map(int,input().split())
dist = [0] * 100001

print(bfs(dist,N,K))





# count = 0
# result = 0
# while(True):
#     if N > K:
#         while N !=K:
#             N -= 1
#             count += 1
#     elif N == K:
#         result = count
#         break
#     else:
#         if 2 * N <= K:
#             while 2 * N < K:
#                 N = N * 2
#                 count += 1
#         elif N < K :
#             while N < K:
#                 N +=1
#                 count +=1
# print(result)



