for tc in range(1,int(input())+1):
    N = int(input())
    T = [0] * ( N + 1 )  # tree이다.
    cnt = 1
    def inorder(v):
        global cnt
        if v> N : return # 끝낸다.
        T[v] = cnt
        cnt +=1
        inorder(v*2)  # 부모
        inorder(v*2 + 1) # 자식

    inorder(1) # 1 번루트를 타고내려가면서
    print(T)

# 천재적이야..