def inOrder(v):
    #왼쪽자식이 있을때
    if len(arr[v]) >= 3:
        inOrder(int(arr[v][2]))
    #출력
    print(arr[v][1], end="")
    #오른쪽자식 있을때.
    if len(arr[v])==4:
        inOrder(int(arr[v][3]))


for tc in range(1, 11):
    N = int(input())

    #2차원리스트로 인접리스트느낌으로 처리
    # 0번인덱스 버리기
    arr = [[]] #미리 하나 넣어두어서 사용 x

    for i in range(N):
        arr.append(input().split())


    print("#{}".format(tc), end=" ")
    inOrder(1)
    print()