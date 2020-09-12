T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rectangle = [1, 3]
    for i in range(2, N//10):
        num = rectangle[i-1] + rectangle[i-2] * 2
        rectangle.append(num)

    print("#{} {}".format(tc, rectangle[(N//10)-1]))