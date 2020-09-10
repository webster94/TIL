for t in range(1,11):
    N = int(input())
    count = 0
    arr = [list(map(int,input().split())) for _ in range(100)]
    for i in range(100):
        flag = False
        for j in range(100):
            if arr[j][i] == 1:
                flag = True:
            elif arr[j][i] ==2 and flag ==True:
                flag = False
                count +=1

    print("#{} {}".format(t,count))