def check(stage):
   x,y = stage
   grade = 1
   for a in arr:
       if x < a[0] and y < a[1]:
           grade +=1
   print(grade , end = " ")


N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
# print(arr) // 입력 잘받음

for i in arr:
    check(i)