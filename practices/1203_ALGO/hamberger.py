import sys
sys.stdin = open('hamberger.txt','r')
def powerset(index,sum_flavor = 0 , sum_kal = 0):
    global max_flavor
    if sum_kal > L : return
    if max_flavor < sum_flavor: max_flavor = sum_flavor
    if index ==N: return
    flavor, kal = arr[index]
    powerset(index+1, sum_flavor + flavor, sum_kal+ kal)
    powerset(index+1,sum_flavor,sum_kal)
T = int(input())
for t in range(1,T+1):
    N,L = map(int,input().split())
    arr = []
    for _ in range(N):
        T,K = map(int,input().split())
        arr.append([T,K])
    # 모든 수열 나열 후, 칼로리의 합이 1000이 넘어간 것은 모두 자르고,  맛에대한 점수가 가장 높은 점수를 출려
    max_flavor = 0
    powerset(0)
    print('#{} {}'.format(t,max_flavor))