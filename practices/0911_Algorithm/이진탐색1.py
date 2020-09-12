# 1부터 N 까지의 자연수를 이진탐색 트리에 저장하려한다.
# 이진탐색트리는 왼쪽 서브트리으 ㅣ루트, 현재노드, 오른쪽 서브 트리의 루트규칙만족
def binary(n):
    global cnt
    if n > N: return
    binary(2*n)  # 중위 순열
    T[n] = cnt
    cnt +=1
    binary(2*n +1)

T = int(input())
for t in range(1,T+1):
    N = int(input())
    T = [0] * (N+1)
    cnt = 1
    binary(1)
    print("#{} {} {}".format(t,T[1],T[N//2]))
