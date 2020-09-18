def binarySearch(Page,key):
    start = 1
    end  =  Page
    count = 0
    while start <= end:
        middle = (start +end )//2
        if middle == key:
            return count
        elif middle > key:
            end = middle
        else : start = middle
        count += 1
T = int(input())
for t in range(1,T+1):
    P,A,B = list(map(int,input().split()))
    A_count = binarySearch(P,A)
    B_count = binarySearch(P,B)
    if A_count < B_count:
        print(f'#{t} A')
    elif A_count == B_count:
        print(f'#{t} 0')
    else:
        print(f'#{t} B')