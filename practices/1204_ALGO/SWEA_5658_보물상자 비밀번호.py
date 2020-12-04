import sys
sys.stdin = open('보물상자.txt','r')
def convert(arr):
    global result
    for i in range(0,len(arr),L):
        key =''.join(arr[i:i+L])
        result.add(key)
    return result

T =int(input())
for t in range(1,T+1):
    N,K = map(int,input().split())
    L = N // 4
    numbers = input()
    result = set()
    convert(numbers)
    # 자물화 구현 완료
    # 이제 numbers를 3번만 돌리는 기능 구현!
    cnt = 0
    numbers = list(numbers)
    while cnt < L:
        end= numbers.pop(-1)
        numbers.insert(0,end)
        convert(numbers)
        cnt +=1
    result = list(result)
    change = []
    for i in result:
        change.append(int(i,16))
    change.sort(reverse=True)
    print('#{} {}'.format(t,change[K-1]))



