# display

- display : block
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지한다.
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.
  - ex) div/ul/ol/li/p/hr/form 등
- display : inline
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지한다.
  - width,heigh,margin-top, margin-bottom을 지정할 수 없다.
  - 상하 여백은 line- height로 지정한다.
  - ex) span/a/img/input,label/b,em,i,strong 등

```
#속성에 따른 수평 정렬

margin- right : auto; 는 오른쪽에 마진을 채우니 왼쪽에 정렬이되는 것

인라인은 말그대로 이동!
```



# CSS position

문서 상에서 요소를 배치하는 방법을 지정한다.

> static: 디폴트 값 (기준 위치)
>
> 아래는 좌표 프로퍼티(top,bottom,left,right)를 사용하여 이동이 가능하다.(음수 가능)
>
> - relative : static 위치를 기준으로 이동
> - absolute : static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(절대위치)
> - fixed : 부모 요소와 관계 없이 브라우저를 기준으로 이동(고정 위치)
>   - 스크롤시에도 항상 같은 곳에 위치
> - 

EMMET

https://docs.emmet.io/cheat-sheet



css layout

> 어디에 놓을지 제어하는 기술
>
> float flexbox, Grid에 대해서 배울 것이다.

# float  어떻게 쓰지?

>이미지 주변에 텍스트로 감싸기 위한 도구,
>
>좌측상단,우측에 띄어줄 수 있다.

```
float - NOne,left, right
```

 더미 필요시 Lorem + teb +enter

```
    .clearfix::after{
      content : "";  빈 블록 만들고
      display : block;  움직이게 못하게하고
      clear: both;  left,right를 초기화한다.
    }빨간색이 뜨더라도 무시를하는!
    float속성을 적용한 요소의 부모요소에 적용한다.
    질문하기!
    
    after 가상 태그를 만들어서 사용
    .after
    영역을 해제하려면
    .clear :
    	clear: left;
    }
    clear : both;
    
```

column wrap질문 1개



# flexbox 는 4개

> 요소 간 공간 배분과 정렬 기능을 위한 1차원 레이아웃
>
> 요소와 축을 기억!!
>
> 요소
>
> - Flex container(부모 요소)
> - Flex Item (자식 요소)
>
> 축
>
> - main axis (메인축)
> - cross axis (교차축)

```
부모에게 flex-container:
display:flex; 값을 준다!
```

##### Flex에 적용하는 속성

1. 배치방향설정 (메인축 방향 변경)  기본 x축 >> 상하 (y축)  

> 메인 축을 중심으로 생각하자 . 크로스 축은 메인의 크로스형.

	2. 메인축 방향 정렬

> justify - content 
>
> justify는 메인

3. 교차축 방향 정렬

> align - items, align-content, align-self
>
> align는 교차

```
self = 1개 1줄
content = 여러 줄
items = 한 줄
```



부모 에 플랙스 선언시 

행으로 나열

메인축으로 시작선에서 시작한다.

채워진다.

```
justify 균등분대, 좌우간격등분, 균등좌우정렬
```



메인축을 줌심으로 컬럼이 어디인지 생각한다! <중요>



# Bootstrap

> 빠르고 반응형 

> 세계에서 가장 유명한 프론트 앤드 소스 툴킷

> responsive grid system!

1. reboot >> normalize

```
RESET : 공격적인, 다 없애준다!
NORMALIZE.css : 나머지브라우저들을 IE에 맞춰줘서 웹표준이 동작하게 한다.
```

2. spacing

mx = 좌우

my = 상하

padding 

margin

012345 



3. breakPoint ><< 그리스시스템에서 확인.
4. resonsive Web : one source로 muilti use!

# bootstrap Grid system

> flex box  로 구성

> 12개의 column 약수가 가장 많아서
>
> 2개의 브레이크 포인트



```
class = container !
class = row >> flex- container

class = col >> flex inline
```

화면을 100%로 맞춰주는게 뭐지??

> > width - 100 이다. 
> >
> > ```
> > 단 나누기
> > flexbox에서 열을 새 줄로 나누려면 작은 해킹이 필요 width: 100%합니다. 열을 새 줄로 줄 바꿈하려는 위치에 요소를 추가 하십시오. 일반적으로 이것은 여러 .rows 로 수행 되지만 모든 구현 방법이이를 설명 할 수있는 것은 아닙니다.
> > ```
> >
> > ![](TIL.assets/image-20200813015221413.png)
> >
> > ```html
> > <div class="container">
> >   <div class="row">
> >     <div class="col-6 col-sm-3">.col-6 .col-sm-3</div>
> >     <div class="col-6 col-sm-3">.col-6 .col-sm-3</div>
> > 
> >     <!-- Force next columns to break to new line -->
> >     <div class="w-100"></div>
> > 
> >     <div class="col-6 col-sm-3">.col-6 .col-sm-3</div>
> >     <div class="col-6 col-sm-3">.col-6 .col-sm-3</div>
> >   </div>
> > </div>
> > ```

네스틴 = 그리드 안에 그리드.

```
송교수님
부트스트랩을 왜 쓰느냐
col 을 통해 화면 레이아웃을 이용
container에서 참조
col , col-md, col-xl 이해해야한다.

```

```
컬럼 레이아웃 해보기 equrl 상자!!
```

```##

부트스트랩에서!
1.수직정렬
2. offset 미리 읽고오기!!  
3. 페이스북 - 아예 요소 안보이게 하기.
components
butten bts btn 컴포넌트 구경하기.
nav 바에 비슷한게 있을 것이다.
navar
가로정렬..ㅎㅎ 이런거 찾아보기.
```

## 수직정렬![image-20200813015616861](TIL.assets/image-20200813015616861.png)

```html
flexbox 정렬 유틸리티를 사용하여 열을 수직 및 수평으로 정렬합니다. Internet Explorer 10-11은 플렉스 컨테이너에 min-height아래와 같이 가있는 경우 플렉스 항목의 수직 정렬을 지원하지 않습니다 . 자세한 내용은 Flexbugs # 3을 참조하십시오.


<div class="container">
  <div class="row align-items-start">
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
  </div>
  <div class="row align-items-center">
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
  </div>
  <div class="row align-items-end">
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
  </div>
</div>

```

![image-20200813015731178](TIL.assets/image-20200813015731178.png)

# 수평정렬

![image-20200813020657874](TIL.assets/image-20200813020657874.png)

```html
<div class="container">
  <div class="row justify-content-start">
    <div class="col-4">
      One of two columns
    </div>
    <div class="col-4">
      One of two columns
    </div>
  </div>
  <div class="row justify-content-center">
    <div class="col-4">
      One of two columns
    </div>
    <div class="col-4">
      One of two columns
    </div>
  </div>
  <div class="row justify-content-end">
    <div class="col-4">
      One of two columns
    </div>
    <div class="col-4">
      One of two columns
    </div>
  </div>
  <div class="row justify-content-around">
    <div class="col-4">
      One of two columns
    </div>
    <div class="col-4">
      One of two columns
    </div>
  </div>
  <div class="row justify-content-between">
    <div class="col-4">
      One of two columns
    </div>
    <div class="col-4">
      One of two columns
    </div>
  </div>
</div>
```





# 오프셋

> ### 열 오프셋
>
> 반응 형 `.offset-`그리드 클래스와 [마진 유틸리티](https://getbootstrap.com/docs/4.5/utilities/spacing/) 의 두 가지 방법으로 그리드 열을 오프셋 할 수 있습니다 . 그리드 클래스는 열과 일치하도록 크기가 조정되는 반면 여백은 오프셋 너비가 가변적 인 빠른 레이아웃에 더 유용합니다.
>
> #### 오프셋 클래스
>
> `.offset-md-*`클래스를 사용하여 열을 오른쪽으로 이동합니다 . 이러한 클래스는 열의 왼쪽 여백을 열 단위로 늘 `*`립니다. 예를 들어, 4 개 열 위로 `.offset-md-4`이동 `.col-md-4`합니다.

![image-20200813015946643](TIL.assets/image-20200813015946643.png)