N =int(input())
arr = set()
for _ in range(N):
    arr.add(input())
arrlength = []
for i in arr:
    arrlength.append((len(i),i))
arrlength.sort()
for i in arrlength:
    print(i[1])