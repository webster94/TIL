T = int(input())
for t in range(1,T+1):
    calender = input()
    year = calender[:4]
    month = calender[4:6]
    day = calender[6:]
    threeone = [1,3,5,7,8,10,12]
    threezero = [4,6,9,11]
    twoeight= [2]

    if int(month) in threeone:
        if int(day) > 31:
            print(-1)
        else:
            print(f'#{t} {year}/{month}/{day}')
    elif int(month) in threezero:
        if int(day) >30:
            print(f'#{t} -1')
        else:
            print(f'#{t} {year}/{month}/{day}')
    elif int(month) in twoeight:
        if int(day) >28:
            print(f'#{t} -1')
        else:
            print(f'#{t} {year}/{month}/{day}')

    else:
        print(f'#{t} -1')