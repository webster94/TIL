from collections import Counter
import sys
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
print("%.f"%(sum(arr)/N))
arr.sort()
print(arr[len(arr)//2])
bindo = {}
cnt = 0
for i in arr:
    bindo[i] = bindo.get(i,0) +1

valuebindo =sorted(bindo.items(), key=lambda x: x[1] , reverse=True)
k = Counter(arr).most_common()
if len(k) > 1:
    index = 0
    if k[0][1] == k[1][1]:
        print(k[1][0])
    else:
        print(k[0][0])
else:
    print(k[0][0])
keybindo = sorted(bindo.items())
if len(keybindo) > 1 :
    last = len(keybindo)
    print(keybindo[last-1][0] - keybindo[0][0])
else:
    print(0)