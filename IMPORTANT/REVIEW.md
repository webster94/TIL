거꾸로 사과 나열하기

```python
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



2. ```python
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

```python
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

```python
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

```python
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

```python
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

## 7.23일 Practice

```python
#1 아래에 코드를 작성하시오.
abs() 직접 구현하기
절댓값은 숫자형 자료(int, float)가 들어오면 절댓값을 반환하고, 복소수형 자료(complex)가 들어오면 해당하는 자료의 크기를 반환합니다.

파이썬 내장 함수 abs()를 직접 구현한 my_abs()를 작성하시오

#def my_abs(x):
#    if x >= 0 :
#        return  x 
#    elif type(x) == complex :
#        return (x.real**2 + x.imag**2)**0.5
#    else:
#        return -x
def my_abs(x):
    if type(x) ==complex:
        return (x.imag**2+x.real**2)**(1/2)
    else :
        if x <0:
            return -x
        elif x == 0:
            return x **2
        else :
            return x
```

```python
# 아래의 코드를 실행하여 출력된 결과를 확인하시오.
print(my_abs(3+4j))
print(my_abs(-0.0))
print(my_abs(-5))
print(abs(3+4j), abs(-0.0), abs(-5))
```

```python
#2
all() 직접 구현하기
all()은 인자로 받는 iterable(range, list)의 모든 요소가 참이거나 비어있으면 True를 반환합니다.

파이썬 내장 함수 all()을 직접 구현한 my_all()을 작성하시오.

예시)

my_all([]) #=> True
my_all([1, 2, 5, '6']) #=> True
my_all([[], 2, 5, '6']) #=> False
```

```python
# 아래에 코드를 작성하시오.

#def my_all(*list):
#    for i in list:  
#        if i == [0]:  # a가 빈칸인걸 어떻게알까..?   >> bool 을 사용해서 거짓인지 확인하 수가 있었네!!!
#            return False
#            break
#        
#        else:
#            return True
def my_all(elements):
    result = True
    for element in elements:
        if bool(element)== False:# 초기값 설정 true 처음부터 봐야하니까
     #   if not bool(element)
     #   if not elemnet (자동으로 형변환이 된다.)
            result = False
            break
    return result

#def my_all(elements):
#    for element in elements:
#        if not element"
#        return False
#    return Ture
```

```python
# 아래의 코드를 실행하여 출력된 결과를 확인하시오.

print(my_all([]))
print(my_all([1, 2, 5, '6']))
print(my_all([[], 2, 5, '6']))
print(my_all([]), my_all([1, 2, 5, '6']), my_all([[], 2, 5, '6']))
```

```python
True
True
False
True True False
```

```python
#3.# 아래에 코드를 작성하시오.

def my_any(elements):
    result = False
    for element in elements:
        #bool(element) == True
        if element:
            result= True
            break
    return result

```

```python
print(my_any([1, 2, 5, '6']))
print(my_any([[], 2, 5, '6']))
print(my_any([0]))
print(any([1, 2, 5, '6']), any([[], 2, 5, '6']), any([0]))
```

```python
True
True
False
True True False
```

```python
#4.
## 불쌍한 달팽이

> 달팽이는 낮 시간 동안에 기둥을 올라간다. 하지만 밤에는 잠을 자면서 어느 정도의 거리만큼 미끄러진다. (낮 시간 동안 올라간 거리보다는 적게 미끄러진다.)
> 
> 달팽이가 기둥의 꼭대기에 도달하는 날까지 걸리는 시간을 반환하는 함수 `snail()`을 작성하시오.

> 함수의 인자는 다음과 같다.
1. 기둥의 높이(미터)
2. 낮 시간 동안 달팽이가 올라가는 거리(미터)
3. 달팽이가 야간에 잠을 자는 동안 미끄러지는 거리(미터)

---

예시)

​```python
snail(100, 5, 2) #=> 33
def snail(height, day, night):
    result = (height // (day - night))
    return result
강사님!
#def snail(height, day, night):
#    result = (height // (day - night))
#    return result
# while 사용!

def snail (height, day, night):
    # 하루가 시작되면 댈팽이가 기둥을 오른다. 만약에 기둥을 다 오르면 count를 리턴!
    # 달팽이가 미끄러진다
    count = 0
    snail_height = 0
    while True:  # 그냥 돌릴 때 사용!
        count += 1
        snail_height += day
        if snail_height >= height:   # 조건을 만족할 때까지 무한 방법을 사용하는 방법!!!
            return count
        snail_height -= night
print(snail(100, 5, 2))
print(snail(200,6,2))
```

```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하시오.
print(snail(100, 5, 2))
print(snail(200,6,2))
# 해당 코드를 통해 올바른 결과가 나오는지 확인하시오.
print(snail(100, 5, 2))
print(snail(200,6,2))
33
50
```

```python
#5
자릿수 더하기 (SWEA #2058)
자연수 number를 입력 받아, 각 자릿수의 합을 계산하여 출력하시오.

예시)

sum_of_digit(1234) #=> 10
sum_of_digit(4321) #=> 10
```

```python
def sum_of_digit(number):
    total = 0
    for i in str(number):  # 숫자를 문자로바꾸고  for 문 반복을 실시한다
        total += int(i)   total 에  i를 숫자로 바꿔서 더한다!
    return total
    return total
        #  total = 0  # number를 문자화   ,number = [1,2,3,4]
   # for i in range(number): # number를 리스트화
    #    total += number
    #return total
sum_of_digit(12)
```

```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하시오.
print(sum_of_digit(1234))
print(sum_of_digit(4321))
10
10
```

```python
 #1234
    #1*1000 + 2*100 + 3*10 + 4*1   끝에서 접근이 편하다.
    # 1234 % 10 => 4
    # 1234 //10 => 123
    # 123 % 10 => 3
    # 123 // 10 =>12
    # 12 %10 => 2
    # 12//10 =>1
    # 1% 10 = 1
    # 1// 10 = 0  반복문 종료
def sum_of_digit(number):
    total = 0 
    while True:
        remainder = number % 10
        total += remainder
        number = number // 10 # 다음결과가 이것이니까!
        if number = 0:
            return total
print(sum_of_digit(1234))
print(sum_of_digit(4321))
# 재귀함수로 어떻게 해?

def sum_of_digit(number):
    # sod(4321) => 1+ sod(432) => 1+ 2+ sod(43)+> 1+2+3+sod(4)=>1+2+3+4
    ##끝나는 조건 성립시켜야함
    if number<10
        return number
    else:
        remainder = number % 10
        number = number // 10
        return remainder + sum_of_digit(number)
```

```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하시오.
print(sum_of_digit(1234))
print(sum_of_digit(4321))
```

```
1. 이름공간

   ```
   Local scope: 정의된 함수
   Enclosed scope: 상위 함수
   Global scope: 함수 밖의 변수 혹은 import된 모듈
   Built-in scope: 파이썬안에 내장되어 있는 함수 또는 속성
   ```

2. 답 == 1번

   ```
   1. 함수의 return
   앞서 설명한 것과 마찬가지로 함수는 반환되는 값이 있으며, 이는 어떠한 종류(의 객체)라도 상관없습니다.
   
   단, 오직 한 개의 객체만 반환됩니다. << 그럼 이건 무슨 소린가..
   return a,b ???
   
   함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아갑니다.
   4.가변(임의) 인자 리스트(Arbitrary Argument Lists)
   앞서 설명한 print()처럼 개수가 정해지지 않은 임의의 인자를 받기 위해서는 가변 인자 리스트*args를 활용합니다.
   
   가변 인자 리스트는 tuple 형태로 처리가 되며, 매개변수에 *
   로 표현합니다.
   
   ```

3. 재귀 함수

   ```
   자기 자신을 호출하는 재귀함수는 알고리즘 구현시 많이 사용된다.
   코드가 더 직관적이고 이해하기 쉬운 경우가 있다.
   팩토리얼 재귀함수를 Python Tutor에서 확인해보면, 함수가 호출될 때마다 메모리 공간에 쌓이는 것을 볼 수 있다.
   이 경우, 메모리 스택이 넘치거나(Stack overflow) 프로그램 실행 속도가 늘어지는 단점이 생긴다.
   파이썬에서는 이를 방지하기 위해 1,000번이 넘어가게 되면 더이상 
   ```

   ```python
   def fact(x):
     number = 1
     for i in range(1,x+1):
     
       number *= i
   
     return number
   fact(5)
   ```

   ```python
   def factorial (num):
       return num * factorial(num-1) if num > 1 else 1
      직관적이고 이해하기 쉽다!
   
   ```

   
```

```
1.

​```python
#ask code 1번 숫자의 의미
def get_scret_word(numbers):
    # 65,85,120,
    word = ''
    for number in numbers:
        word += chr(number)
    return word
get_scret_word([83,115,65,102,89])
​```

2.

​```python
def get_secret_number(word):
    number = 0
    for char in word:
        number += ord(char)
    return number
print(get_secret_number('tom'))
​```

3.

​```python
def get_strong_word(word1, word2):
    number1 = 0
    number2= 0
    
    for char in word1:
        number1 +=ord(char)
    for char in word2:
        number2 +=ord(char)
        
    return word1 if number1>=number2 else word2

print(get_strong_word('tom','john'))
​```

​```python
def get_strong_word(word1, word2):
    return word1 if get_secret_number(word1)>= get_secret_number(word2) else word2
print(get_strong_word('tom','john'))
​```


```

