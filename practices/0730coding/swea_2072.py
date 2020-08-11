import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1,T+1):
    #results = input().split() ## 리스트화!
    #results_int = []
    #for result in results:
    #    results_int.append(int(result))
    numbers = map(int,input().split()) 
    ### input().split() 안에 ['1','2','3']이 들어오면
    # [int('1'), int('2'),int('3')]으로 바꿔준다 
    #>> 담긴 수를 하나하나 봐서 홀수이면 토탈에 더한다.
    total = 0
    for number in numbers:
        if (number%2) ==1:
            total += number
    print(f'#{test_case} {total}')




