import sys
sys.stdin = open("view.txt","r")
for t in range(1,11):
    ga = int(input())
    arr = list(map(int,input().split()))
    ans = 0
    for i in range(2, ga-2):
        total = 1231242
        for j in range(-2,3):
            if j != 0 and arr[i] - arr[i+j] < total:
                total = arr[i]- arr[i+j]
        if total > 0:
            ans += total

    print(ans)
