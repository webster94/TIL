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

이제 보니 알았다!! 

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

- 고지식한 패턴 검색 알고리즘 ```okey!```
- 카프-라빈 알고리즘```x```
- KMP 알고리즘```x```
- 보이어-무어 알고리즘```x```

> 고지식한  패턴 검색 알고리즘만 알겠따 ㅎㅎ 0825



노연관 __

보충 때 입력텍스트 받아오는 방법임.

![image-20200824195802379](TIL-Algorithm.assets/image-20200824195802379.png)





오늘 현우랑 공부할 것.

1. 완전탐색  ㅁ 

2. 사전으로 풀어보기.ㅁ 

   - 사전으로 숫자들이 몇개인지 기입하는 논리

   - 흐름

     - dictionary 선언  bin[i] = bin.get(i,0)=1 을 하면 내가 원하는 사진에 값의 개수 를 부여할 수 있었다.
     - for문을  words 다돌리기
     - 요소를 키값에 넣고 중복된 키값의 개수를 count
     - 0부터 개수만큼 나열

     

     현우 스터디 강조사항 ㅁ 

     > 제목은 영어!  파일위치확인에 문제가 발생할 수 있다.
     
     


# 알고리즘 

> 0825  = 오늘은 하루종일 숫자나열, 고지식한 패턴분석, 회순1,2 문제 풀었다..

![image-20200825093036608](TIL-Algorithm.assets/image-20200825093036608.png)

>  GNS 문제 풀이 

파이참 단축키

```
시프트 엔터 내려감

컨트롤 d 복사

alt + shift 방향키 = 움직임

control + y 잘라냄

자동들여쓰끼 = control art + l



- 회문 2개
- 
```

- sort()와 sorted의 차이

  > 원본을 수정하느냐 마느냐의 차이이다.
  >
  > sort()가 원본을 수정하고 sorted는 원본을 수정하지않고 정렬만 해준다.

---

> 20200824일에 고지식한 패턴 검사를 배웠다면
>
> 20200825일은 벽만드는 법을 배우겠다.

- 벽만드는 것

```
T = int(input())                                    # tc개수

def pal_check(line):                                # 회문 체크 수업시간함수
    for idx in range(len(line) // 2):
        if line[idx] != line[-idx - 1]:
            return False
    return True

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    found = False                                   # 루프 깨줄 변수
    arr = [list(input()) for _ in range(N)]
    print('#{}'.format(tc), end = " ")
    for i in range(N):
        for j in range(N - M + 1):
            sample = arr[i][j:j + M]                # 가로
            sample2 = [a[i] for a in arr[j:j + M]]  # 세로
            if pal_check(sample):                   # 가로에서 회문 찾을 경우
                print(''.join(sample))              # 하나로 합쳐주기
                found = True                        # 찾았다
                break
            elif pal_check(sample2):                # 세로에서 회문 찾을 경우
                found = True                        # 찾았다
                print(''.join(sample2))
        if found:                                   # 회문 1개뿐이므로 찾았으면 루프 깨주기
            break

```

```python
GNS
num_list = ["ZRO ", "ONE ", "TWO ", "THR ", "FOR ", "FIV ", "SIX ", "SVN ", "EGT ", "NIN "]
num_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

T = int(input())

for tc in range(1, T + 1):
    a, b = input().split()

    arr = list(input().split())

    cnt = [0] * 10

    for key in arr:
        cnt[num_dict[key]] += 1

    print("#{}".format(tc))

    for i in range(10):
        print(num_list[i] * cnt[i], end="")
    print()
```

```python
행렬찾기

#행렬의 사이즈를 찾는 함수
def search_size(r, c):
    r_cnt = 0
    c_cnt = 0

    for i in range(r, N + 2):
        if arr[i][c] == 0:
            break
        r_cnt += 1
    for j in range(c, N + 2):
        if arr[r][j] == 0:
            break
        c_cnt += 1

    ans.append([r_cnt, c_cnt])

    init(r, c, r_cnt, c_cnt)

#구한 행렬을 0으로 초기화 시키는것
def init(r, c, r_cnt, c_cnt):
    for i in range(r, r + r_cnt):
        for j in range(c, c + c_cnt):
            arr[i][j] = 0


T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    #전체적인 띠를 두르는 작업
    arr = [0] * (N + 2)
    arr[0] = arr[N + 1] = [0] * (N + 2)

    for i in range(N):
        arr[i + 1] = [0] + list(map(int, input().split())) + [0]

    ans = []

    for i in range(1, N + 2):
        for j in range(1, N + 2):
            if arr[i][j] != 0:
                search_size(i, j)

    #정렬, 행렬크기 기준, 같다면 행크기 기준
    ans = sorted(ans, key=lambda x: ((x[0] * x[1]), x[0]))

    print("#{} {}".format(tc, len(ans)), end=" ")
    for i in range(len(ans)):
        print("{} {}".format(ans[i][0], ans[i][1]), end=" ")

    print()
```

---

# 알고리즘 강의 3일차

> 0826

- 오늘의 핵심은 DFS!

![image-20200826095122576](TIL-Algorithm.assets/image-20200826095122576.png)

> 스택, 재귀호출, DFS를 확실하게 알아야한다!!



스택의 특성

> ​	물건을 쌓아 올리듯 자료를 쌓아 올린 형태0의 자료 구조이다.
>
> ex ) 접시를 쌓아 올린 구조!
>
> 2차원 배열은 내가 적은 코드의 줄에 비례한다.. 공감!





스택의 구현

> 빈 스택에 원소 ABC를 차례로 삽입 후 한 번 삭제하는 연산과정
>
> top = -1 을 가리킨다 
>
> 삽입할때는 top에 하나 올리고 그자리에다가 arr[top] = 'a' 넣고
>
> 삭제할 때는 top를 하나 내리고 pop을 한다.

![image-20200826101957221](TIL-Algorithm.assets/image-20200826101957221.png)

> 파이썬의 pop 알고리즘

stack = []

```
## 괄호 검색기
def check(arr):
    for i in range(len(arr)):
        if arr[i] == '(' : # push실시 push는 append~
            stack.append(arr[i])
        elif arr[i] == ')': # pop하고 비교 , 이때 비엇나 확인하기!!
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if stack  : return False  # 괄호에 남아있으면 False! 그렇지않으면 TRUE
    else: return True




stack = []
arr = "()()((()))"
print(check(arr))

```

---

- 함수 호출

![image-20200826105359476](TIL-Algorithm.assets/image-20200826105359476.png)

함수는 시스템에 후입선출로 저장된다.





- 재귀

![image-20200826111106817](TIL-Algorithm.assets/image-20200826111106817.png)

오전 강의 종료 김한욱 교수님 수고하셨습니다

----

오후 양명균 교수님 리뷰

- 스택 

  > 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조이다.

  >  선형구조와 비선형 구조를 갖는다.
  >
  > LIFO 후입선출

- pop

꺼낼께 있어야 꺼낸다.

따라서 0일 경우 return 0을 하거나 non을 표시해준다.

s.pop(-1) 또는 s.pop(0)을 사용해서 스택의 맨위에 있는 것을 삭제한다.





스택은 파이썬스타일(추가하는 append)와 c언어 스타일(스택을 넉넉하게 미리 설정하는 방법)이 있다.

메모장

```
push//pop

def push():

top += 1

 return 

def pop():

if len(s) == 0:

​	return None

else:

top -=1

return pop()


```





0826 알고리즘오후 김한욱 교수님

---

### Memoization

> 메모이제이션!!



![image-20200826141420277](TIL-Algorithm.assets/image-20200826141420277.png)



# DP  (오늘의 핵심)

![image-20200826143124626](TIL-Algorithm.assets/image-20200826143124626.png)

![image-20200826143627195](TIL-Algorithm.assets/image-20200826143627195.png)

dp 예

![image-20200826143942854](TIL-Algorithm.assets/image-20200826143942854.png)

> 재귀는 함수로 되어잇지만 db는 for문으로 되어있다.

![image-20200826164702405](TIL-Algorithm.assets/image-20200826164702405.png)

>  다른 예.

# *오늘의 핵심!! 교수님 풀강조했따.*

![image-20200826150104851](TIL-Algorithm.assets/image-20200826150104851.png)

> 선형구조 : 배열

1. 표현 : 메모리에 저장  표현하는 방법이 다르다. 
   - **인접 행렬로 표현하는 방법**
   - **인접 리스트**
   - 간섭의 배열
2. 순회: DFS BFS 두가지 방법이있다.

![image-20200826151119988](TIL-Algorithm.assets/image-20200826151119988.png)

> G = grapht
>
> 시작 정점  =V
>
> 정점 주변   W 

![image-20200826152142117](TIL-Algorithm.assets/image-20200826152142117.png)

![image-20200826153354069](TIL-Algorithm.assets/image-20200826153354069.png)

연필로 그려가보면서 하자.

연습문제1

![image-20200826153545712](TIL-Algorithm.assets/image-20200826153545712.png)

7 8 

1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 

---

보충 tip !!

알파벳을 문자열로 변환할때 유용한 방법임

문자 >> 인트로 맵핑하기 위한 문자열

arr = list(input()) 한줄 읽고, 리스트로 변환(문자)

![image-20200826192204723](TIL-Algorithm.assets/image-20200826192204723.png)

내가 찾고싶은 문자열을 리스트로 만들어서 만들수있다.!

![image-20200826192959101](TIL-Algorithm.assets/image-20200826192959101.png)



- 2차원 배열!

  

N,M = map(int,input().split())

mylist = [0 for i in range(N)] # 1차원 배열 초기화

list(map(int,input().split()))  # 1차원 배열 입력받아서 >> 리스트(1차원)로 이동

mylist[0] = list(map(int,input().split()))

mylist[0] = list(map(int,input().split()))

mylist[0] = list(map(int,input().split()))

> > for i in range(N)"
> >
> > mylist[i] = list(map(int,input().split()))
>
> > > 



파리채

```
T = ``int``(input())
for` `t in range(1,T+1):
  ``N,M = list(map(``int``,input().split()))
  ``flys = [[``int``(x) ``for` `x in list(map(``int``,input().split()))] ``for` `_ in range(N)] # 대입완료
  ``maxfly = 0
  ``for` `i in range(N-M+1):
    ``for` `j in range(N-M+1):
      ``totalfly = 0
      ``for` `a in range(M):
        ``for` `b in range(M):
          ``totalfly += flys[i+a][j+b]
        ``if` `maxfly < totalfly:
          ``maxfly = totalfly
  ``print(f``'#{t} {maxfly}'``)
```

잘배워간다 채린

```
T = int(input())
for t in range(1,T+1):
    # 먼저 파리부터 입력을 받자.
    N , M = map(int,input().split())
    flies = []
    for i in range(N):
        flies.append(list(map(int,input().split())))
    # 파리가 이제 채에 올라왔다. 잡으러가야지!
    killed = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for k in range(M):
                total += sum(flies[i+k][j:j+M])
            killed.append(total)
    print(max(killed))
```

```
​```python
for tc in range(1, TC+1): #case를 받고, 
    N, M = map(int, input().split()) #n,m을 각각 받는다
    result = [] #펠린드롬을 받을 result

    #가로줄 확인
    Garo_lst = [] #1 가로 빈리스트에 data를 넣는다
    for i in range(N): #2
        Data = input() 
        Garo_lst.append(Data) 
        for i in range(len(Data)-M+1):#4 가로줄 체크! 
           if Data[i:M+i] == Data[i:M+i][::-1]:#5
            result.append(Data[i:M+i])

    #세로줄 확인
    Sero_lst = [] #6  빈리스트와 빈 문자열
    Sero_sub_lst = ''#7
    for x in range(N): #8  n을 한번에 돌리네
        for y in Garo_lst:#9 문자열의 행
            Sero_sub_lst += y[x] #10  에 열을 넣고 
        Sero_lst.append(Sero_sub_lst) #11 
        Sero_sub_lst ='' #12

    for sero_data in Sero_lst:
        for j in range(len(sero_data)-M+1):
            if sero_data[j:M+j] == sero_data[j:M+j][::-1]:
                result.append(sero_data[j:M+j])

    # print(result)
    print("#%d %s"%(tc, result[0])) #13
​```

#1 : Garo_lst를 만들어줌, 이 리스트는 나중에 컬럼대로 뽑을때 사용할려고 만든거임

#2 : N만큼 돌면서, 한줄한줄 문자열을 입력받고, 미리 만들어놓은 Garo_lst에 추가한다.

#3 : 한 행의 길이 len(Data)에서 찾아야할 패턴의 길이인 M을 빼주고 +1을 더해준다.

#4 : 한행씩 보면서 i번째부터 i+M까지 자른 문자열이 뒤에서 읽은 것과 같다면 그건 펠린드롬이기 때문에

#5 : result에 담아놓는다

#6 : 이제 세로줄을 확인해야하는데, 일단 Garo_lst처럼 Sero_lst를 만들어줘야 한다.

#7 : 칼럼대로 쭉 읽어서 저장할 Sero_sub_lst를 만들어주고

#8 : 세로길이 만큼 돌면서(세로로 도는거임)

#9 : 미리 만들어놓은 가로 리스트를 돌면서(아래로 하나씩)

#10 : Sero_sub_lst에다가 세로로 읽은 칼럼을 쭉 뽑아서 저장할건데, 이게 헷갈렸다. 이중 for문은 두번째로 들어가는 for문이 일을 많이하는거다. 여기서 0번째 칼럼일때 가로행이 계속 바껴져야한다. 

#11 : 다 뽑았으면 미리 만들어놓은 Sero_list에 저장하고

#12 : 중간정산 변수인 Sero_sub_lst는 초기화한다. 

#13 : !!!!만약에 result=['abcde'] 형태로 되어있는데 'abcde' 형태의 문자열로 뽑을려면 result[0] 하면 됨.나중에도 써야징
```

```
글자 찾기
---
T = int(input())
for t in range(1,T+1):
    str1 = input()
    str2 = input()
    if (str2.find(str1)) >0:
        print(f'#{t} {1}')
    else:
        print(f'#{t} {0}')
---내가 푼것
#교수님 방법1.
    	ans = 0
        if str2.find(str1) != -1:
            ans = 1
        print("{} {}".format(tc,ans))
# 교수님 방법2.
if ans
```

> 브루투방식으로 해봐야함!
>
> 델타 이동의 기본 내가 작성해봐야함..

달팽이!

```python
#우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input()) # 입력받기

for tc in range(1, T+1):
    N = int(input())  #  N*N배열

    arr = [[0] * N for _ in range(N)]   # 0배열 선언

    d = 0 #방향 0 : 우 , 1 : 하, 2 : 좌 , 3 : 상   #방향
    r = 0 # 좌표들
    c = 0
    num = 1 # 시작점

    while num <= N * N:
        arr[r][c] = num #현재칸에 값을 저장장
        num += 1 # 다음 숫자 준비

        #다음칸을 결정
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<= nr <N and 0 <= nc <N and arr[nr][nc] == 0:  # 위에서 우로 바뀔때 중요하다.
            #현재좌표를 갱신
            r, c = nr , nc
        else:
            d = (d+1)%4  # 방향임
            r += dr[d]
            c += dc[d]

    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()
```



---

> 0827 
>
> 오늘은 달팽이만 봤다..

```python
# 달팽이 방향정하고
# 입력받고
# 초기화하고
# 와일문으로 위치변경, 방향변경
# 출력

dr = [0,1,0,-1]
dc = [1,0,-1,0]
T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [ [0] * N for _ in range(N)]
    num = 1 # 시작값
    d= 0 # 방향전환 용
    r = 0 # 좌표용 행
    c = 0 # 좌표용 열 
    while num < N*N:
        arr[r][c] = num
        num +=1
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            r,c = nr,nc # 바뀐 위치로 최신화
        else:# 아닐 경우 방향을 바꿔주자
            d = (d+1)%4
            r += dr[d]
            c += dc[d]
    print("#{}".format(t))
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end=' ')
        print()
```

---

0828 활용법

DFS 스택

```
입력받자
V,E = map을 통해 받고
0번 괄호 만들어서
st,end 포인트를 담는다.
arr[st][ed] = arr[ed][st] ==1가 연결되었음을 표시

빈 괄호에 담아서 기록을 한다.
visited = []
stack []
stack.append(1)
```







미로 코드 짠 모습

![image-20200828112240489](TIL-Algorithm.assets/image-20200828112240489.png)

지워버리는 방법

![image-20200828112650633](TIL-Algorithm.assets/image-20200828112650633.png)

![image-20200828112626253](TIL-Algorithm.assets/image-20200828112626253.png)

재귀

![image-20200828112955601](TIL-Algorithm.assets/image-20200828112955601.png)

농장물 풀기..

회문 1,2

사다리 1,2,

달팽이 , 파리퇴치,

주석달기!!





문제푸는법!

점화식 (문제들의 관계 찾아내기)

재귀호출 ! 오래걸린다면 메모이제이션 추가

반복! 

 #### 사전에서 내림차순 정렬하는 법

![image-20200901002004757](TIL-Algorithm.assets/image-20200901002004757.png)

# 9월 화이팅 !! 알고리즘

![image-20200901101510679](TIL-Algorithm.assets/image-20200901101510679.png)

> 부분집합 출력하기



---

0901 공부한 것은 부분집합과 순열의 차이이다.

순열은 제시된 숫자에서 가능한 배열을 모두 나열한 것이고

부분집합은 모든 집합을 나열한 것이다. 따라서, 코드의 차이는 부분집합은

 길이가 idx와 같아졌을 때, 포문을 돌려 visited가 1이 되는 모든 arr[i]를 출력한다.

또한, visited 배열을 1로 만들고 다시 0을 만들어서 지나온 곳을 다시 갈 수 있도록 한다.



순열은 다르다 순열은 n == k 가 같아졌을 때, 그 때의 sel(순열조합문장)만 프린트하고

visited 가 1이 된 곳을 다시 가지않기 위해  함수호출을 적게 한다.



아래의 코드를 참고하자.

```python
arr = [8,3,2]
N = 3
visited = [0] * N
def powerset(n,k):
    if n == k :
        for i in range(n):
            if visited[i]:
                print(arr[i],end = " ")
        print()
    else:
        visited[k] = 1
        powerset(n,k+1)
        visited[k] = 0
        powerset(n,k+1)
powerset(N,0)
```

> 모든 부분집합 출력

``` python
N = 3
sel = [0] * N
visited = [0] * N
arr = [1,2,3]

def perm(N,idx):
    if N == idx:
        print(sel)
        return
    for i in range(N):
        if not visited[i] :
            sel[idx] = arr[i]
            visited[i] = 1
            perm(N,idx+1)
            visited[i] = 0
perm(N,0)

```

>  순열 출력