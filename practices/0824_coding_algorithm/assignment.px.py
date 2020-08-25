# - dictionary 선언
# - for문을  words 다돌리기
# - 요소를 키값에 넣고 중복된 키값의 개수를 count
# - 0부터 개수만큼 나열

T = int(input())
for t in range(1,T+1):
    result = ''
    test = input()
    numbers = input().split()
    bin = {}
    for i in numbers:
        bin[i]=bin.get(i,0)+1
    li = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for cherry in li:
        result += (cherry+' ') *bin[cherry]
    print(f'#{t} {result}')
