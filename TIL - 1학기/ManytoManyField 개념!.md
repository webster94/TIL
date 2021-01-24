# ManytoManyField 개념!

![image-20200928094733029](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928094733029.png)



DB  Representation (데이터베이스에서의 표현)

django는 M:N 관계를 나타내는 중개 테이블을 만든다.

테이블 이름은 MANYTOMANYFIELD의 이름과 이를 포함하는 모델의 이름을 조합하여 생성한다.

ex) accounts_doctors_patient



- Argument

![image-20200928095117258](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928095117258.png)

![image-20200928100759120](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928100759120.png)

하나의 유저 > 여러 article 좋아요가능

하나의 article  > 여러 user가 좋아요가능

MODEL!

![image-20200928101118161](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928101118161.png)



Related-name을 반드시 사용해야 할 때

![image-20200928101501387](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928101501387.png)

동일한 코드 발생

![image-20200928101521648](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928101521648.png)

![image-20200928101535569](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928101535569.png)

1. urls

   ![image-20200928103632721](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928103632721.png)

2. views

![image-20200928104752975](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928104752975.png)

![image-20200928104900636](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928104900636.png)

좋아요 코드임.



3. html

인덱스에서 detail 위 에 작성!

![image-20200928105209082](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928105209082.png)

4. 이미지 만들기

font awesome

에서 버튼에 코드 넣었음.

![image-20200928110900165](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928110900165.png)

![image-20200928111310814](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928111310814.png)

![image-20200928111615844](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928111615844.png)

views 수정

![image-20200928111944076](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928111944076.png)

> 위에 방법이 더 권장된다. in 보단 하나를 찾아야하는 상황에서는 exist를 사용해야한다.

![image-20200928112500131](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928112500131.png)

![image-20200928131456770](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928131456770.png)

![image-20200928163034796](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200928163034796.png)