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

# 7.24  REVIEW

> # 
> #1번은 홀수는 2를 곱하고 짝수는 3을 곱한 숫자들을 합한 합을 나타내는 코딩
>
> #2 소수 구별 소수는 y, 아니면 n
> #3  소수 구별 2번째
> #4 numbers = [26, 39, 51, 53, 57, 79, 85]  소수 인지 아닌지 출력하는 함수
> #5 가운데 숫자 출력 함수 짝수는 2개 출력하는 함수
> #6 어떤 값을 받고 평균을 구하는 함수   <
> #7리스트안에 숫자들을 모두 더하는 함수
> #8 리스트안 특정한 항목만의 합을 더하는 함
>
> - 사전 만들어서 풀기 
>
>   #9 리스트안에 리스트들의 숫자들의 합을 모두 더하는 함수 
>
> - all_list_sum([[1],[2,3],[4,5,6],[7,8,9,10]]) 
>
> #10 입력받은 글자의  a 제거하기
>
> #11. 5의 갯수 구하기  
>
> - numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
> - 
>
> #12. 최댓값 등장횟수 구하기
>
> - 최댓값 등장횟수 구하기
>   numbers = [7, 10, 22, 7, 22, 22]
>
> #13. 이영희씨 이름 횟수 구하기.
>
> - students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
>
> #14. `abs()` 직접 구현하기
>
> > 절댓값은 숫자형 자료(int, float)가 들어오면 절댓값을 반환하고, 복소수형 자료(complex)가 들어오면 해당하는 자료의 크기를 반환합니다.
> >
> > 예시)
> >
> > ```python
> > my_abs(3+4j) #=> 5.0
> > my_abs(-0.0) #=> 0.0
> > my_abs(-5) #=> 5
> > ```
> >
> > 파이썬 내장 함수 `abs()`를 직접 구현한 `my_abs()`를 작성하시오.
>
> #15.`all()` 직접 구현하기
>
> > `all()`은 인자로 받는 iterable(range, list)의 모든 요소가 참이거나 비어있으면 True를 반환합니다.
> >
> > 파이썬 내장 함수 `all()`을 직접 구현한 `my_all()`을 작성하시오.
> >
> > 
> >
> > print(my_all([]))
> > print(my_all([1, 2, 5, '6']))
> > print(my_all([[], 2, 5, '6']))
> > print(my_all([]), my_all([1, 2, 5, '6']), my_all([[], 2, 5, '6']))
> >
> > ```
> > True
> > True
> > False
> > True True False
> > ```
>
> #16`any()` 직접 구현하기
>
> `any()`는 인자로 받는 iterable(range, list)의 요소 중 하나라도 참이면 True를 반환하고, 비어있으면 False를 반환합니다.
>
> 파이썬 내장 함수 `any()`을 직접 구현한 `my_any()` 함수를 작성하시오.
>
> 예시)
>
> ```python
> my_any([1, 2, 5, '6']) #=> True
> my_any([[], 2, 5, '6']) #=> True
> my_any([0]) #=> False
> ```
>
> #17 불쌍한 달팽이
>
> > 달팽이는 낮 시간 동안에 기둥을 올라간다. 하지만 밤에는 잠을 자면서 어느 정도의 거리만큼 미끄러진다. (낮 시간 동안 올라간 거리보다는 적게 미끄러진다.)
> >
> > 달팽이가 기둥의 꼭대기에 도달하는 날까지 걸리는 시간을 반환하는 함수 `snail()`을 작성하시오.
>
> > 함수의 인자는 다음과 같다.
> >
> > 1. 기둥의 높이(미터)
> > 2. 낮 시간 동안 달팽이가 올라가는 거리(미터)
> > 3. 달팽이가 야간에 잠을 자는 동안 미끄러지는 거리(미터)
>
> > 
>
> #18.자릿수 더하기 (SWEA #2058)
>
> > 자연수 number를 입력 받아, 각 자릿수의 합을 계산하여 출력하시오.
>
> ------
>
> 예시)
>
> ```python
> sum_of_digit(1234) #=> 10
> sum_of_digit(4321) #=> 10
> ```

```

```

+ 7.23 연습문제들 추가해야한다.





# 이론복습

