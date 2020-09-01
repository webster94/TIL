#입력을 받고
# 8자리를 리스트에 if를 사용
# 월> 일을 순으로
# 월은 4,6,9,11 // 1,3,5,7,8,10,12 //2 월
T = int(input())
for t in range(1,T+1):
    numbers = input()
    result = []
    li30 = [4,6,9,11]
    li31 = [1,3,5,7,8,10,12]
    print(numbers[4:6])
    if int(numbers[4:6]) in li30:
        if int(numbers[6:8]) <= 30:
            
            # print(f'#{t} {numbers[:4]}/{numbers[5:6]}/{numbers[6:7]}')
        else:
            print(-1)
    elif int(numbers[4:6]) in li31:
        if int(numbers[6:8]) <= 31:
            # print(f'#{t} {numbers[:4]}/{numbers[5:6]}/{numbers[6:7]}')
        else:
            print(-1)
    else:
        if int(numbers[4:6]) ==2:
            if int(numbers[6:8]) <= 28:
                # print(f'#{t} {numbers[:4]}/{numbers[5:6]}/{numbers[6:7]}')
            else:
                print(-1)