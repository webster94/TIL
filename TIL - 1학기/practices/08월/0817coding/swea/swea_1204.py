# 최빈수 출력
# .count를 이용해서 큰수부터 카운터를 최빈수를 뽑아내자
T = int(input())
for t in range(1,T+1):
    test = int(input())
    numbers = list(map(int,input().split()))
    max_num = 0
    max_count = 0
    for i in range(100,1,-1):
        count = numbers.count(i)
        if max_count < count:
            max_count = count
            max_num = i
    print(f'#{t} {max_num}')
