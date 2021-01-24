# 배수의 숫자들을 글자로 바꾼뒤 숫자로 다시 바꿔서 set에 추가한다음
# 셋의 길이가 10이 되는 번쨰 수를 출력하자
# 입력부분
T = int(input())
for t in range(1,T+1):
    N = int(input())
    result = set()
    i = 1
    cnt = 0
    while True:
        number = str(N*i)
        for num in number:
            result.add(int(num))
        cnt = cnt + 1
        i = i+1
        if len(result) == 10:
            print(f'#{t} {number}')
            break;




