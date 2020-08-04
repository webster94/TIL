'''
# 1. 입력 T,n,n개의 숫자
# 2. n개의 숫자를 모두 탐색하는데 각 숫자가 몇개 있는지 찾아야됨.
# 3. 찾고나서 n개의 숫자들을 다시 돌면서 max_cnt max_num
4. max_cnt로 비교를 하되 자기보다 큰 카운트가 나오면 max_cnt, max_num 최신화
5. 나랑 카운트가 같다 동시에 나보다 값이 큰놈이면 max_num을 최신화
'''
T = int(input())
for t in range(1,T+1):
    count = int(input())
    max=-1
    max_i=-1
    string = list(map(int,input()))
    for char in string:
        string_count = 0
        string_num=-1
        for j in string:
            if char == j:
                string_count += 1
                string_num=j
        if max < string_count:
                max = string_count
                max_i = string_num
        elif max == string_count:
            if max_i < char:
                max_i = char
    print(f'#{t} {max_i} {max}')

