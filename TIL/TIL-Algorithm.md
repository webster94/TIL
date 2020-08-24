# 알고리즘!  

> 2020 0824

![image-20200824100307472](C:\Users\MinHo\AppData\Roaming\Typora\typora-user-images\image-20200824100307472.png)

- 패턴매칭은 blue to force이다.. 이게 뭔가..? 이것부터 알아야한다.
  - 컴퓨터의 힘을 쓴다는 뜻
  - kmp
  - 보이어-무어
- 문자열 표현!
  - 메모리에는 숫자를 저장한다.

### ASC

 **ASKII  7 bit 인코딩**으로 128문자(0~127)를 표현하며 33개의 출력 불가능한```/0 null```문자 제어 문자들과 공백을 비롯한 95개의 출력가능한 문자들로 이루어져있다.

Byte의 정의?  

> 영문자 한자를 나타내는 단위다.
>
> 100byte 영어단어 100자가 저장된 것이구나.

parity bit(짝수,홀수)  = 에러를 체크할 수 있다.

0001000  > 1의 개수를 짝수로 만들자  그러기 위해선 1을 더한다. 

00010101 이 오면 짝수개가 아닌 것을 판단하기위해 페리티 비트를 사용한다.



 ### 아스키코드

![image-20200824102755839](C:\Users\MinHo\AppData\Roaming\Typora\typora-user-images\image-20200824102755839.png)

> 외우면 좋은 것
>
> A = 65
>
> a = 97 
>
> 대문자 소문자 변환 시 32만큼의 변화가 있다는 것을 알아야한다.
>
> 0은 48번
>
> 32번 앞에는 출력되지않는 것들이다.

---



유니코드!!를 다시 character Set으로 분류한다.

utf (UTF - UNICODE TRANSFORMATION FORMat) - 8 1,2,3,4비트를 각각 사용할 수 있다. 한글은 3비트!

파이썬은 utf-8 이다.

자바는 utf-16이다.

---

python 은 char 타입이 없음 . string으로 처리를 함

보통 c에서는 문자 'A' , "ABC" 로 구분하지만 python에선s 'abc' 나 ABC'나 동일하다.그래서 더할 수도 있도 있고 ''' /''' 연결도 가능하다 . *3 을 하면 반복도 된다!

### 문자열 뒤집기

![image-20200824110247666](C:\Users\MinHo\AppData\Roaming\Typora\typora-user-images\image-20200824110247666.png)

- 알고리즘

![image-20200824110309176](C:\Users\MinHo\AppData\Roaming\Typora\typora-user-images\image-20200824110309176.png)

![image-20200824110354180](C:\Users\MinHo\AppData\Roaming\Typora\typora-user-images\image-20200824110354180.png)

4번을 돌리면 된다. 알고리즘이 문자열인데 바꾸기가 될까?

절대 안된다!! 리스트함수를 사용해서 리스트로 바꿔서 적용해야한다.

str이 아닌 arr을 가지고 해야한다.

다 끝나고 "".join(arr)을 해주면 문자열로 바뀌게 된다.

str > list

swap

list> str로 바꾼다.



```python
sentence = 'algorithm'
result = ''
print(sentence)
sentence=list(sentence)
print(sentence)
sentence[0],sentence[8] = sentence[8],sentence[0]
sentence[1],sentence[7] = sentence[7],sentence[1]
sentence[2],sentence[6] = sentence[6],sentence[2]
sentence[3],sentence[5] = sentence[5],sentence[3]
sentence=''.join(sentence)
print(sentence)
```

```python
def str_rev(str):
    arr = list(str)
    for i in range(len(arr)//2):
        arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
    str = ''.join(arr)
    return str
    # ----------------
str = "algorithm"
str1 = str_rev(str)
print(str1)
```

```python
s = "algorithm"
s = s[::-1]
print(s)
```

```
양명균교수님버전
```

![image-20200824124724476](TIL-Algorithm.assets/image-20200824124724476.png)

오후 수업



```
test = '1+2'
print(test) 
print(repr(test)) 문자열 표시를 해준다.
print(eval(repr(test)))  eval은 벗겨준다!
print(eval(eval(repr(test))))
```

```
결과
1+2
'1+2'
1+2
3
```

![image-20200824143601199](TIL-Algorithm.assets/image-20200824143601199.png)

필요한 순간이 올것이다..

16진수를 10진수로 바꿀 떄는 ord (c) - ord [a] + 10



문자열도 비교가 가능하다.

abc <abd  로 나온다 아스키 코드 덕분이다!

```python
def atoi(str):
    value = 0
    for i in range(len(str)):
        c = str[i]
        # # 0~ 9
        # if c >= '0'and c <= '9':
        if '0' <= c <= '9':
            digit = ord(c) - ord('0')
        else:
            break
        value = value*10 +digit
        return value

a= '123'
# a= [1,2,3]
print(type(a))
b = atoi(a)
print(type(b))
```





리스트!

![image-20200824144638636](TIL-Algorithm.assets/image-20200824144638636.png)

여기부분 헷갈렸다!!

```python
def itoa(num):
    x = num # 몫
    arr = []
    y = 0 # 나머지
    while x:
        y = x % 10
        x = x // 10
        arr.append(chr(y + ord('0'))) # 문자열을 만들려고!
    arr.reverse()
    str = "".join(arr)
    return str

x= 123
print(x,type(x))
str = itoa(x)
print(str,type(str))


```

![image-20200824151223897](TIL-Algorithm.assets/image-20200824151223897.png)

 둘의 차이가멀까

---

# 오늘의 핵심

![image-20200824151431838](TIL-Algorithm.assets/image-20200824151431838.png)

---

고지식한 방법..

잘 모르겠군

![image-20200824152747887](TIL-Algorithm.assets/image-20200824152747887.png)

 

역시 모르겠군..

![image-20200824154537297](TIL-Algorithm.assets/image-20200824154537297.png)



아는것!

양명균 교수님 

---

== 과 is의 차이

a= [1,2,3]

b = a

c = [1,2,3]

파이썬 ==  값을 비교하는 것이다.

is 는 주소값이 같은지 확인

print(a is b) true

print(a is c ) false  (id가 다르기 때문에, 서로 다른 객체이다.)

---



알고리즘

- 고지식한 패턴 검색 알고리즘
- 카프-라빈 알고리즘
- KMP 알고리즘
- 보이어-무어 알고리즘



노연관 __

보충 때 입력텍스트 받아오는 방법임.

![image-20200824195802379](TIL-Algorithm.assets/image-20200824195802379.png)





오늘 현우랑 공부할 것.

1. 완전탐색 

2. 사전으로 풀어보기.

   - 사전으로 숫자들이 몇개인지 기입하는 논리

   - 흐름

     - dictionary 선언
     - for문을  words 다돌리기
     - 요소를 키값에 넣고 중복된 키값의 개수를 count
     - 0부터 개수만큼 나열

     

     현우 스터디 강조사항

     

3. 달력문제

