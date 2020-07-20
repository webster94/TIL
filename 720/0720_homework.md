1.

```
import keyward
print(keyward.kwlist)
```



```python
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

2.

```python
import math
import sys
num1 = 0.1 *3  # 0.300000000004
num2 = 0.3  # 0.3 // num1과 num2값이 다르다.
print (num1)
print(num2)  
abs(num1-num2) <= sys.float_info.epsilon  # epsilon을 활용하여 비교한 결과
math.isclose(num1,num2) # math를 활용하여 비교한 결과 
```

>sys와 math를 활용한 결과 True가 나왔고 같다는 것을 비교해서 확인했다.

3.

```python
print(" \"\\n\"을 활용해서 \n줄을 바꿀 수 있다.")
print(" \"\\t\"을 활용해서 띄어\t쓰기를 할 수 있다.")
print(" \'\\\'을 활용해서 백슬\\래시를 사용할 수 있다.")
```

```
 "\n"을 활용해서 
줄을 바꿀 수 있다.
 "\t"을 활용해서 띄어	쓰기를 할 수 있다.
 '\'을 활용해서 백슬\래시를 사용할 수 있다.
```



4.

```python
name = '철수'
print('안녕 %s야'%name)
print('안녕 {}야'.format(name))
print(f'안녕 {name}야)
```

```결과
안녕 철수야
안녕 철수야
안녕 철수야
```

5.

```python
str(1) # =1
int('30') # 30
int(5) # 5
bool('50') # True
int('3.5') # invali literal for int() withbase 10 : '3.5'
```

6.

```python
n = 5
m = 9
print("""'*''*''*''*''*'
'*'\t    '*'
'*'\t    '*'
'*'\t    '*'
'*'\t    '*'
'*'\t    '*'
'*'\t    '*'
'*'\t    '*'
'*'\t    '*'
'*'\t    '*'
'*'\t    '*'
'*''*''*''*''*'
""")

```

```결과
'*''*''*''*''*'
'*'	        '*'
'*'	        '*'
'*'	        '*'
'*'	        '*'
'*'	        '*'
'*'	        '*'
'*'	        '*'
'*'	        '*'
'*'	        '*'
'*'	        '*'
'*''*''*''*''*'
```



7.

```python
print(" \"파일은 c:\\windows\\Users\\내문서\\Python에 저장이 되었습니다.\" \n 나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'")
```

``` 결과
 "파일은 c:\windows\Users\내문서\Python에 저장이 되었습니다." 
 나는 생각했다. 'cd를 써서 git bash로 들어가 봐야지.'
```

8.

```python
a=2
b=6
c=2
num1 = (-(b)+ float(((b**2 - 4*a*c)**0.5))/2*a
num2 = (-(b)- float((b**2-4*a*c)**0.5))/2*a
print(num1)
print(num2)
```

```결과
-1.5278640450004204
-10.47213595499958
```

