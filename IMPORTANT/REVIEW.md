거꾸로 사과 나열하기

```
words = input()



\# 아래에 코드를 작성하시오.

'''

for word in reversed(words):

 print(word, end='')

'''

\#x = len(words) 

\#for i in range(x): 

\# print(words[x - i -1], end=" ")

\# apple를 뒤집어서 작성할 때

\# 1. 맨 뒷문자부터 확인해서 작성

\# 2. 맨 처음부터 확인하긴하는데. 작성을 맨 뒤부터 

reversed_word = ''



for index in range(len(words)-1,-1,-1): #?????

   char = words[index]

   reversed_word += char

print(reversed_word)
```



2. ```
   a 제거하기
   words = input()
   
   # 아래에 코드를 작성하시오.
   
   #for word in words:
    # if word == a :
     #  continue
      # print(word)
     #print(word)
   
     # 사용자 입력이 복잡 ~~
     # 문자를 하나하나 보면서 a인지 확인한 후
     # a가 아니라면 답안에 작성
   result = ''# 빈 문자열!!
   for char in words:
       if char != 'a':
         result = result+char
   print(result)
   ```

3.  5개수 구하기

```
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

# 아래에 코드를 작성하시오.
#numbers를 모두 돌면서
# 5가 나오면  count +1한다
count = 0
for number in numbers:
  if number ==5:
    count += 1
print(count)
print(numbers.count(5))
```

```
최댓값 등장횟수 구하기
numbers = [7, 10, 22, 7, 22, 22]

# 아래에 코드를 작성하시오.
# 최대값과 등장횟수를 기억하고 있어야한다.
# 최대값은 기존 최대값보다 더 큰 값이 나오면 갱신, 이때 등장횟수도 1으로 초기화
# 최대값과  같은 숫자가 나오면 등장횟수를 +1

#maxi = max(numbers)
#print(maxi)
#print(numbers.count(maxi))
max_num = numbers[0]
count = 0

for number in numbers:
    if max_num < number:
       print('max_number 갱신')
       max_num = number 
       count = 0
    if max_num == number:
       count += 1
print(max_num,count)
```

```
최솟값 구하기
numbers = [7, 10, 22, 4, 3, 17]

# 아래에 코드를 작성하시오.

#print(min(numbers))
max_number = numbers[0]
for number in numbers:
    if max_number < number:
        max_number = number
print(max_number)

```

```
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

# 아래에 코드를 작성하시오.
# 투표결과를 보는데, 학생이름이 이영희면, 카운트를 +1 한다.

#student = '이영희'
#print(students.count('이영희'))
count = 0
for student in students:
    if student == '이영희':
        count += 1
print(count)
```

