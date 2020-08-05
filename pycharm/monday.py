
for t in range(1,11):
    test_num = int(input())
    buildings = list(map(int,input().split()))
    total = 0
    for building in range(2,len(buildings)-2):
        li = [buildings[building-1],buildings[building-2],buildings[building+1],buildings[building+2]]
        max2 = max(li)
        if buildings[building]>=max2:
            a = buildings[building]-max2
            total +=a
    print(f'#{t} {total}')