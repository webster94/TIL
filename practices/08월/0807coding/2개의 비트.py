# 4bit >> 0~15
#4bit 1이 2번 포함된경우
# 1100,1010,1001
for bits in range(1<<4) : #모든 경우의수
    cnt = 0
    for i in range(4):
        if bits & (1<<i):
            cnt +=1

    if cnt ==2:
        for i in range(3,-1,-1):
            if bits % (1<<i): print(1,end= '')
            else: print(0,end = '')
        print()