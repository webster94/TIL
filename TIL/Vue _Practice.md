SPA는 Single Page Application의 약자이다. 

모델뷰 뷰모델 = MVVM

M = templates

view = html 부분

viewmodel은 중간에 script안의 공간이다. mtv로 따지면, 컨트롤러의 역할이다.



a =message

b= new Vew

c = '#app'





view 순서

1. html 빈 껍데기 생성
2. data 정의, 바인딩 (시간에 따라 변한다.)
3.  method 작성

데이터를 잡아서, src에 넣고 클릭하면 나오게끔 출력해보자!

1. scr에 데이터를 넣을 방법
2. 데이터 집어내기



Vue에서

1. function 키워드로 선언하는 경우
   - 2번이 아닌 경우
2. 화살표 함수로 선언하는 경우 
   - 익명함수 일 때 사용





중요한 차이가 있느 경우

 this를 함수 안에서 쓸 때 function을 써보니 window가 나올 경우 화살표를 사용해야한다

윈도가 나오면 바꿔서 써야한다..





view순서

1.T,F,F 단방향이 아니다.

3 . v-for, v-if, num