# 7.20 workshop

1. 세로로 출력하기

   ```python
   number = int(input('자연수를 입력하시오 : '))
   
   # 아래에 코드를 작성하시오.
   for _ in range(1,number+1):
       print(_)
   ```

   ```결과
   자연수를 입력하시오 : 22
   1
   2
   3
   4
   5
   6
   7
   8
   9
   10
   11
   12
   13
   14
   15
   16
   17
   18
   19
   20
   21
   22
   ```

   

2. 가로로 출력하기

   ```python
   number = int(input('자연수를 입력하시오'))
   
   # 아래에 코드를 작성하시오.
   for _ in range(1,number+1):
     print(_, end =' ')
   
   ```

   ```결과
   자연수를 입력하시오22
   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 
   ```

   

3. 거꾸로 세로로 출력하기

   ```python
   number = int(input('값을 입력하시오 : '))
   
   # 아래에 코드를 작성하시오.
   print(number)
   while number > 1 :
     number = number -1
     print(number)
   ```

   

   ```결과
   값을 입력하시오 : 3
   3
   2
   1
   ```

   

   4. 거꾸로 출력해보아요

     ```python
   number = int(input('값을 입력하시오'))
   
   # 아래에 코드를 작성하시오.
   while number >= 0 :
       print(number ,end = ' ')
       number = number -1
    
   
     ```

   ```결과
   값을 입력하시오6
   6 5 4 3 2 1 0 
   ```

   

   ​	5.N줄 덧셈

     ```python
   number = int(input('값을 입력하시오 : '))
   
   hap = 0
   i = 0 
   for i in range(1,number+1):
       hap = hap + i
       i = i+1
   print(hap)
   
   
   
     ```

   ```결과
   값을 입력하시오 : 10
   55
   ```

   