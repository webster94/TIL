# The Basic of Python 

> 2020.7.20(월) 0930~ 1130



### 1.`목표` 

  Software 개발 과정 학습!



### 2. `개요`

 프로그래밍은 `저장`, `제어` 로 나뉜다.

- 저장 

`무엇을` = `data type` 을

`어떻게 ` = `=` 를 사용해서

`어디에` =  `variable, container에 저장한다`



- 제어

  조건, 반복!

### 3. 본론 `문법`

1. 주석

```주석

1.- 한줄 사용 시 #(파운드)으로 표현
2.- 여러줄 사용 시 ``` 또는 ''' 표현
ex ) 1. # 이것은 주석입니다. 
2. ``` 이것은
주석
입니다 
​```
```

2. 코드라인

```
-파이썬 코드는 1줄에 1문장이 원칙이다.
잘못된 ex)
print('hello')print('ssafy') = >>invalid syntax
해결방법
; 사용
print('hello');print('ssafy')

```

3. 변수(variable)

```
- 할당연산자(assignment Operator): =
ex)
a = 'ssafy'
# a 라는 상자에 ssafy라는 글자를 할당한다!

- type 확인방법
해당 데이터 타입 확인 : type()
메모리 주소 확인 : id()

- 식별자(Identifiers)
 > 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름
 > 예약어,내장함수 사용 금지(i.e print(keyword.kwlist))
 
 - 데이터타입(data type)
   #### 숫자
  (1)정수[ingteger] 
  (2)실수[float]
     ex) a = 3.14 or 314e-2
      tybe(b)
       결과 >> float
      
     * 실수의 연산☆☆☆
      print(3.5 - 3.2)
       결과>> 0.2999999
       = 0.3 이 아니다
        
       >>해결방법 2가지
         sys 모듈 방식
         import sys
         print(sys.float_info.epsilon)
         match 모듈 방식
   (3)복소수(complex number)
    1)a= 3+4j 로 표현
    2) 주의할 점은 연산자 주위에 띄어쓰기 금지
  
  
    #### 문자
    * 문자열은 Single qotes(')나 Double quotes(")를 활용하여 표현한다.
       ex) greeting = 'hello'
           tip. # 사용자에게 받은 입력은 기본적으로 str이다.
                number = input('숫자를 입력해주세요 : ')
       			 print(number *2) 
      			결과>> 3 입력시 33이 출력된다. 이는 숫자를 글자로 읽기 때문이다.
  			    글자를 숫자로 인식시키기 위해선
      			print(int(number*2)) 로 한다.
 	* 따옴표 사용 
 	  - 문자열 안에 문장부호 (',")가 사용될 경우 이스케이프 문자(\)를 활용 가능합니다.
 	  - ex "he's \'cool\'"
      - 문자열은 + 연산자로 이어붙이고, *연산자로 반복시킬 수 있습니다.
      - 두개 이상의 문자열이 연속해서 나타나면 자동으로 이어 붙여집니다.
    * 이스케이프 시퀀스
     - \n \t \r \0 \\ \` \``  (사용하면서 알아가자)
     
     *string interpolation ☆☆☆
     name = 'herry'
     초기) # %- formatting
     print('내 이름은 %s입니다'%name)
     중간 # str.format()활용
     print('내 이름은 {}입니다'.format(name))
     결과 # f-string 활용!!
     print(f'내 이름은 {name}입니다')
     
     다양한 형식 활용 datatime 모듈로 오늘 표현
     import datatime
     now = datatime.datatime.now()
     print(now)
     >> 2020-7-20 02:23
     
     #interpolation에서 출력형식 지정할 수 있습니다.
     f'올해는 {now:%y} 이번달은 {now:%m}, 오늘은 {now :%d}'
      >> 올해는 2020 이번달은 07 오늘은 20 
      #string interpolation을 통해 출력형식 지정 뿐만 아니라, 연산도 가능합니다.
     r= 10
     pi = 3.141592
     print(f'{pi:.3}넓이는 : {pi*r*r:.3}')
     넓이는 3.14e+02
```

