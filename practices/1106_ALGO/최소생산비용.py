import sys
sys.stdin = open('최소생산비용.txt','r')
def check(visited,idx,result):
    global ans
    if result > ans :
        return
    if visited == (1<<N) -1: # 111 이 되면!
        ans = min(ans,result) # ans, 와 result 중에 작은것을 ans 에 저장한다.
        return
    for i in range(N):

        if visited & 1<< i : continue # TRue가 나오면 같다는거지 그럼안함 # 같은 행을 가지않게 만듬
        check(visited | 1 << i , idx + 1, result + arr[idx][i]) # 다 가면 111 이 된다.

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0xfffffffff
    for i in range(N):
        check(1<<i , 1, arr[0][i])
    print(ans)