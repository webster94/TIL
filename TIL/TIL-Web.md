# 과목평가 대비

HTML// CSS 



## HTML

HTML

"웹 컨텐츠의 의미와 구조를 정의할 때 사용하는 언어"

HTML 기초
Hyper

텍스트 등의 정보가 동일 선상에 있는 것이 아니라 다중으로 연결되어 있는 상태

Hyper Text

참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근 할 수 있는 텍스트
하이퍼 텍스트가 쓰인 기술등 중 가장 중요한 2가지 (http, html)

Markup Language

특정 텍스트에 역할을 부여하는, 따라서 "마크업을 한다" 라고 하는 건 제목이 제목이라하고 본문이 본문이라고 마킹을 하는 것
ex) h1 tag는 단순히 글자가 커지는 것이 아니라 의미론적으로 그 페이지에서 가장 핵심 주제를 의미하는 것

HTML 기본 구조
DOM

DOM은 문서의 구조화된 표현(structured representation)을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공하여 그들이 문서 구조, 스타일, 내용 등을 변경할 수 있게 도움
DOM은 동일한 문서를 표현하고, 저장하고, 조작하는 방법을 제공
웹 페이지의 객체 지향 표현

요소 (Element)

HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성

태그(Element, 요소)는 컨텐츠(내용)를 감싸서 그 정보의 성격과 의미를 정의 한다.


내용이 없는 태그들

br, hr, img, input, link, meta


요소는 중첩(nested)될 수 있다.

이러한 중첩들로 하나의 문서를 완성해 나간다.
그리고 항상 열고 닫는 태그 쌍이 잘 맞는지 잘 봐야한다.
HTML은 오류를 뿜지 않고 그냥 레이아웃이 깨져버리기 때문에 어떤 면에서는 친절하게 오류 띄워주고 어디 틀렸는지 알려주는 프로그래밍 보다 디버깅이 힘들다.



속성 (Attribute)

속성(Attribute)은 태그의 부가적인 정보가 들어온다.
요소는 속성을 가질 수 있으며 요소에 추가적 정보(이미지 파일의 경로, 크기 등)를 제공한다.
요소의 시작 태그에 위치해야 하며 이름과 값의 쌍을 이룬다.
태그와 상관없이 사용 가능한 속성들(html global attribute)도 있다.


시맨틱 태그

브라우저, 검색엔진, 개발자 모두에게 콘텐츠의 의미를 명확히 설명하는 태그

장점

읽기 쉬워진다. (개발자)

개발자가 의도한 요소의 의미가 명확히 드러나고 있다.이것은 코드의 가독성을 높이고 유지보수를 쉽게 한다.


접근성이 좋아진다. (검색엔진 및 보조기술 → 시력장애용 스크린리더 → 더 나은 경험 제공)

HTML 문서는 html 언어 + 사람이 읽을 수 있는 content의 조합인데, 검색 엔진은 HTML 코드만 잘 읽는다.
그래서 이 검색 엔진이 HTML을 잘 이해하도록 시맨틱 태그 사용이 권장되고, 그러면 검색 엔진도 무슨 내용인지 이해할 수 있게 된다.



시맨틱 웹

웹에 존재하는 수많은 웹페이지들에 메타데이터를 부여하여, 기존의 단순한 데이터 집합이었던 웹페이지를 '의미'와 '관련성'을 가지는 거대한 데이터베이스로 구축하고자 하는 발상.



# WEB

- 접근성이 뛰어나고, 배우기가 수월하다
- 프로젝트 하기 용이하다
- 배우기 빠른 것은 실제 홈페이지들을 들어가서 개발자도구로 분해도 해보고 만들어보고 해봐야됨
- `alt + b`를 누르면 브라우저를 열어 만든 것을 볼 수 있음

### HTML 기본

[HTML 기본 개념에 대해 잘 나와있으니 참고하자!](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/HTML_기본)

[https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/HTML_%EA%B8%B0%EB%B3%B8](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/HTML_기본)

### CSS 기본

CSS 기본 개념! 참고하자!

[https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/CSS_%EA%B8%B0%EB%B3%B8](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/CSS_기본)

### 기본 html 구성

```
<!DOCTYPE html> 이문서가 뭔지 알려주는 라인
<html>
    <head>
        이페이지 정보
    </head>
    <body>
        실제 화면에 표시될 데이터가 담김
    </body>
</html>
```

- 인코딩을 지정해주는 것이 매우 중요함!
- 인코딩 : 컴퓨터는 이진법으로 이루어진 수들만 저장할 수 있는데 어떻게 저장할 지 방식을 지정해주면 다른 컴퓨터에서 열었을 때도 같게 보임
- title은 페이지의 제목 이름을 나타냄

```
<!DOCTYPE html> 
<html>
    <head>
        <meta charset="UTF-8"> 인코딩
        <title>건강 설문</title>    	
    </head>
    <body>
    </body>
</html>
```

- html은 들여쓰기가 안돼있어도 인식됨, 들여쓰기는 보기좋게 하려는 거당. html은 열린태그 닫힌태그 기준으로 작동을 함

### 각각 기능들 설명

- 이미지 삽입, 크기 조정도 가능

```
<body>
   <img src="이미지주소 복사 후 붙여넣기" alt="그 이미지 이름 " width="200px" height="100px">
</body>
```

- `h1`은 크게 제목으로 보여짐
- `p`는 제목과는 다르게 본문 느낌으로 글자가 쓰여짐

```
<body>
	<h1>싸피 데일리 건강 설문</h1>
    <p>싸피에서는 교육생 여러분들의 건강 상태를 매일 매일 확입합니다. 협조 바랍니다.</p>
</body>
```

- `form` 정보를 받을 곳 제출하기를 눌렀을 때 이 정보를 어디로 전달할지 정함
- `action`어떤 정보가 쌓이게 될거고, 내가 action이라는 곳에 전달을 할거다

```
<body>
	<form action="https://www.naver.com"> 
</body>
```

- `div`에 감싸주면 줄이 바뀜

- `label` 입력란 앞에 정보를 적음

- `for`에 name을 적고 아래 `input`에서 `id`로 name을 주면

- 실제 web에서 label 글을 클릭했을 때 input창에 커서가 감

- ```
  input
  ```

   

  사용자로부터 정보를 입력받을 수 있음

  - `name`에 fullname이라는 `key`로 내가 적은 이름(input값)이 value로 전달됨
  - 예) http://naver.com/?fullname=내가적은이름&class-no=2&temp=37.5미만 이런식으로 됨

```
<body>
	<form~>
		<div> 
            <label for="name">이름을 적어주세요</label>
            <input type="text" id="name" name="fullname" value="초기값이 설정됨"> 
</div>        
</body>
```

- (참고) vscode에서 alt+shift+화살표 하면 라인복사가됨
- 태그사이에 있는 이름은 화면에 표시될 text이고 value에 적은 것은 정보가 전달될 때 사용됨

```
<body>
	<form~>
		<div> 
            <label for="class-no">반을 선택 하세요</label>
            <select name="" id="class-no"> 
                <option value="1반">1반</option> 
                <option value="2반">2반</option>
                <option value="3반">3반</option>
                <option value="4반">4반</option>
            </select>
        </div>
</body>
```

- `id`를 `label`과 같게 주면 글자를 클릭했을 때 체크가됨
- `name`을 똑같이 주면 둘중 하나가 선택이 됨

```
<body>
    <div>
        <p>체온</p>
        <label for="under">37.5도 미만</label>
        <input type="radio" name="temp" id="under" value="37.5미만">
        <label for="upper">37.5도 이상</label>
        <input type="radio" name="temp" id="upper" value="37.5미만">
    </div>
</body>            
```

- value설정안하면 그냥 "제출"뜸

```
<body>
        <input type="submit" value="제출하기"> 
    </form> 
</body>
```

#### 구글 검색기 만들어보기

- `name`값은 실제 구글이 검색할 때 쓰는 key 값(쿼리의 약자)
- `https://www.google.com/search?q=`

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>구글 검색기</title>
</head>
<body>
    <h1>구글 검색기</h1>
    <form action="http://www.google.com/search">
        <label for="keyword">검색어를 입력하세요:</label>
        <input type="text" id="keyword" name="q">
        <input type="submit" value="검색">
    </form>
</body>
</html>
```

## 시멘틱 태그

- 문서에 의미를 부여

- 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현

- 단순히 구역을 나누는 것 뿐만 아니라 의미를 가지는 태그들을 활용하기 위한 노력

- Non semantic 요소는 div, span등이 있으며, h1,table 태그 들도 시멘틱 태그로 볼 수 있음

- 검색엔진최적화(SEO)를 위해서 메타태그, 시멘틱 태그 등을 통한 마크업을 효과적으로 할 필요가 있음

- header

- nav

- aside

- section

- article

- footer

- 장점

  1. 읽기가 쉬워진다(개발자입장)

  - 개발자가 의도한 요소의 의미가 명확히 드러남
  - 코드의 가독성을 높이고 유지보수를 쉽게 함

  1. 접근성이 좋아진다

  - 검색엔진 -> 시력장애용 스크린리더 -> 더 나은 사용자 경험을 제공

### 그룹컨텐츠

- `<p>`
- `<hr>`
- `<ol>` 등

### 텍스트 관련 요소

- <a> : 하이퍼링크
- `<b>` vs `<strong>` : 글자를 굵게 만들어줌(b는 그냥 굵게, strong은 강조를 함-스크린리더가 읽을때 강조를 해줌)
- `<i>` vs `<em>` : 글자 기울림(i는 그냥 이탤릭체, em은 이탤릭체로 강조를 한다는 의미가 부여되어 있음)
- `<br>` :줄바꿈

### form

- `<form>`은 서버에서 처리될 데이터를 제공하는 역할
- 기본속성
  - action : 어디로 보낼지 결정을 함
  - method : GET(이번주에는 이거로 사용할거야), POST 방식이 있음

### input

- 다양한 타입을 가지는 입력 데이터 필드
- `<label>` : 서식 입력 요소의 캡션
- 공통속성
  - name, placeholder
  - required
  - autofocus

## CSS

CSS

스타일, 레이아웃 등을 통해 HTML이 사용자에게 어떻게 표시 되는지를 지정하는 언어
사용자에게 문서(HTML)를 표시하는 방법을 지정하는 언어


CSS 구문

구문은 선택자와 함께 열린다.
스타일을 지정할 html 요소를 선택.
다음 중괄호가 있는데 이 안에는 속성과 값 쌍 형태를 가지는 하나 또는 그 이상의 선언(declaration)이 있다.
각 쌍은 우리가 선택한 요소의 속성을 지정하고 속성에 부여할 값을 지정한다.

선언문

속성 (Property)

사람이 읽을 수 있는 식별자로, 어떤 (글꼴, 너비, 배경색 등) 스타일 기능을 변경할지 나타냅니다.


값 (Value)

각 속성에는 값을 부여한다.
값은 어떻게 (글꼴을 이걸로, 배경 색을 저걸로 등)스타일 기능을 변경할 건지 나타낸다.



CSS 정의 방법

Inline style
내부 참조 (Embedding style)
외부 참조 (Link style)



CSS Selector

선택자는 스타일을 지정할 웹 페이지의 HTML 요소를 대상으로 하는 데 사용

클래스(class) 선택자

클래스 선택자는 마침표( .) 문자로 시작 하며 해당 클래스가 적용된 문서의 모든 항목을 선택

아이디(id) 선택자

아이디 선택자는 # 문자로 시작하며 기본적으로 클래스 선택자와 같은 방식으로 사용
그러나 아이디는 문서 당 한 번만 사용할 수 있으며 요소에는 단일 id값만 적용 할 수 있다
문서에서 동일한 아이디를 여러 번 사용해도 동작하나 그렇게 하면 안된다.

복합 선택자

자손(하위의 모든 요소) : 셀렉터a  공백 셀렉터b
자식(바로 아래의 요소) : 셀렉터a > 셀렉터b

적용 우선순위


!important

다른 사람들의 코드에서 발견할 때 그 의미를 알 수 있는 것은 좋다.
하지만 반드시 필요한 경우가 아니면 절대 사용하지 않는 것이 좋다.,

!important 는 cascading이 정상적으로 작동하는 방식을 변경하므로, CSS 스타일 문제를 해결하기가 어렵습니다.


inline style
id 선택자

id는 대부분의 다른 선택자보다 우선순위가 높기 때문에 다루기가 어려워 질 수 있다.
대부분의 경우 id 보다는 모두  class 선택자로 작성하는 것이 좋다.
만약 문서 내 링크 이동이나 for를 사용하는 특별한 경우에만 아이디를 사용한다.


class 선택자
요소 선택자
소스 순서



CSS 단위
(상대) 크기 단위
px

모니터 해상도의 한 화소인 '픽셀'을 기준
픽셀의 크기는 변하지 않기 때문에 고정적인 단위

%

백분율 단위
가변적인 레이아웃에서 자주 사용

em

em은 상속의 영향 받음, rem은 최상위 요소(html)를 기준으로 결정됨.
상황에 따라 각기 다른 값을 가질 수 있다.

rem

최상위 요소인 html(root em)을  절대 단위를 기준으로 삼음. 상속의 영향을 받지 않음.
상속에 영향을 받지 않기 때문에 대부분의 경우 rem 을 많이 사용한다.

viewport

(스크롤을 내리지 않은 상태에서) 웹 페이지를 방문한 유저에게 현재 보이는 웹 컨텐츠의 영역
viewport를 기준으로한 상대적인 사이즈
주로 스마트폰이나 테블릿 디바이스의 화면을 일컫는 용어로 사용된다.
vw, vh

색상 표현 단위

색상 키워드

색상 키워드는 대소문자를 구분하지 않는 식별자로, red, blue, black처럼 특정 색을 나타낸다


RGB 색상

빨강, 초록, 파랑을 통해 특정 색을 표현
16진수 표기법이나 함수형 표기법으로 사용
a는 alpha(투명도)가 추가된 것


HSL 색상

색상, 채도, 명도를 통해 특정 색상을 표현
a는 alpha(투명도)가 추가된 것





Box Model

웹 디자인은 contents를 담을 box model을 정의하고 CSS 속성을 통해 스타일(배경, 폰트와 텍스트 등)과 위치 및 정렬을 지정하는 것.


모든 HTML 요소는 box 형태로 되어있다.
하나의 박스는 네 부분(영역)으로 이루어 진다.

content / padding / border / margin




Content

글이나 이미지, 비디오 등 요소의 실제 내용


Padding (안쪽 여백)

Border(테두리) 안쪽의 내부 여백
배경색, 이미지 지정 가능


Border
Margin (바깥쪽 여백)

테두리 바깥의 외부 여백
배경색 지정 불가



마진 상쇄

block의 top 및 bottom margin이 때로는 (결합되는 마진 중 크기가) 가장 큰 한 마진으로 결합(combine, 상쇄(collapsed))된다.



Display

display CSS 속성은 요소를 블록과 인라인 요소 중 어느 쪽으로 처리할지와 함께 자식 요소를 배치할 때 사용할 레이아웃을 설정한다.

block

쌓이는 박스
요소는 블록 요소 상자를 생성하여 일반 흐름에서 요소 앞뒤에 줄 바꿈을 생성한다.
블록 레벨 요소안에 인라인 레벨 요소가 들어갈 수 있다.

inline

줄바꿈이 일어나지 않는 행의 일부 요소
content 너비만큼 가로 폭을 차지
width, height, margin-top, margin-bottom을 지정할 수 없음
상하 여백은 line-height로 지정

inline-block

inline 처럼 텍스트 흐름대로 나열, block처럼 박스 형태이기 block 속성 사용가능.

none

해당 요소를 화면에서 사라지게 하며 요소의 공간조차 사라지게 한다.

visibility: hidden;은 해당 요소를 화면에서 사라지게는 하나 공간은 사라지지 않는다.



Position
박스의 위치 속성 & 값

position

static / absolute / relative / fixed
z-index



기본 개념

static (기본 위치)

모든 태그의 기본
태그의 default 값


relative (상대 위치)

기본 위치(static)를 기준으로 좌표 속성을 사용해 위치 이동


absolute (절대 위치)

static 이 아닌 부모/조상 요소를 기준으로 좌표 속성 만큼 이동
부모 요소를 찾아가고 나아가 없다면 body에 붙는다.


fixed (고정 위치)

부모/조상 요소와 관계없이 브라우저의 viewport를 기준으로 좌표 속성 만큼 이동
스크롤을 내리거나 올려도 화면에서 사라지지 않고 항상 같은 곳에 위치



absolute


absolute는 원래 위치해 있었던 과거 위치에 있던 공간은 더 이상 존재하지 않는다는 점이 특징이다.
즉, 다른 모든 것과는 별개로 독자적인 곳에 놓이게 된다.
언제 쓸까?

페이지의 다른 요소의 위치와 간섭하지 않는 격리된 사용자 인터페이스 기능을 만들 수 있다.
팝업 정보 상자 및 제어 메뉴, 롤오버 패널, 페이지 어느 곳에서나 끌어서 놓기할 수 있는 유저 인터페이스 페이지 등

- - 

## CSS(Cascading Style Sheets)

- 스타일과 레이아웃을 통해 문서(html)를 표시하는 방법을 지정하는 언어
- `{}` 선택자(selector)
- 그 아래 `선언`의 요소는 `속성:값;`이렇게 이루어져 있다.
- 정의 하는 방법
  - 인라인 : 해당 태그에 직접 style 속성을 활용(한줄로 작성)
  - 내부 참조 :`head`태그 안에 `style`태그의 css구문이 들어가 있다.
    - 수업진행은 이거로 할 예정
  - 외부참조: 외부 CSS파일을 `head`내 `link`를 통해 불러오기
    - 기본적으로는 일반적인 방법
    - 반복되는 구문들을 외부참조로 두고 내부 각각에 지정해줄 것을 내부참조로 적기도 함
- 속성은 다 외우는 것이 아니라 주로 쓰는 것 정도만 알아두자..

### 선택자

- HTML 문서에서 특정한 요소를 선택하여 스타일링 하기 위해서는 반드시 선택자라는 개념이 필요
- 기초 선택자
  - 전체, 타입, 클래스, 아이디, 속성
- 선택 선택자 위에서 부터 하나씩 실행되는데 마지막에 있는 h2에 지정된 오렌지색에 의해 덮어씌어진 것임
- h3과 h4에 적용 한줄씩 띄어줌(웹표준 표기)

```
<head>
    <style>
    * {
      color: red;
    }
    h2 { 
        color: orange;
    }
    h3,
    h4 { 
      font-size: 10px;
    }
    .green { 
      color: green;
    }
    #purple { 
        color: purple;
    }
    .box > p { 
      font-size: 30px;
    }
    .box p {
      color: blue;
    }
  </style>
```

- `*` 전체 선택자
- 전체에 적용하겠다라는 뜻
- `.` 클래스 선택자
  - 클래스를 생성(다중표기가능)
  - 웬만하면 클래스 선택자를 이용해서 스타일 지정!
  - 클래스를 두개를 주고 싶다면 공백을 주고 연달아 적으면 됨 쉼표는 적으면 안됨!
  - `<h1 class="green box">SSAFY</h1>`
  - 이렇게 쓰면 적용됨(다중으로 다른 곳에 적어도 가능)
  - 클래스를 두개 주고싶다면 공백을 주고 쉼표없이 연달아 적으면됨
- `#` id선택자
  - 문서상에서 유일한 선택자만 명시하기 위해 하는것
  - 다중으로 선택해서 하면 안됨 해도 오류는 안나지만 그렇게 쓰지말기!!
- 자식선택자 `>`
  - `.box > p {` box클래스 바로 안에 있는 p태그(두단계아래는 안되고 바로 아래!직계자손만..)
  - `.box p {` 클래스 안의 모든 p태그를 바꿔줌

### 우선순위

- 중요도
- `!important`
  - 사용시 주의! 반드시 필요한 경우가 아니면 절대 사용하지 않는게 중요하다
  - CSS는 아래로 흐르는데 이건 흐름을 끊어버림 오류가 나면 디버깅하기 어려워짐
  - 웬만하면 다 클래스 선택자로 사용!
- 인라인 >id 선택자 >class 선택자 >요소선택자 >소스코드

```
<style>
    p {
      color: orange;
    }
    h2 {
      color: darkviolet !important;
    }
    .blue {
      color: blue; 
    }
    .green {
      color: green; 
    }
    #red {
      color: red; 
    }
  </style>
</head>
<body>
  <p>1</p>
  <p class="blue">2</p>
  <p class="blue green">3</p>
  <p class="green blue">4</p>
  <p id="red" class="blue">5</p>
  <h2 id="red" class="blue">6</h2>
  <p id="red" class="blue" style="color: yellow;">7</p> #우선순위가 인라인이 더 높아서 이건 안바뀌고 색 그대로
  <h2 id="red" class="blue" style="color: yellow;">8</h2>
</body>
```

- ```
  !important;
  ```

  - 인라인보다 더 높은 우선순위에 의해 덮어씌어짐

- ```
  요소선택자
  ```

  - h2태그는 important에 의해 무조건 보라, 나머지는 파랑으로

- ```
  .class
  ```

  - 클래스 두개가 적용돼있다면 적힌 순서가 중요한게 아님
  - `<p class="green blue">4</p>`
  - style에 마지막으로 선언된 green클래스에 의해 4,5 둘다 green이 됨

- ```
  #id
  ```

  - 5번 선택자 우선순위에서 class보다 id가 높기 때문에 바뀜 id가 우선순위가 높은편이라 실제로는 클래스로 다 만드는게 유지보수에 편함
  - id는 링크이동, 라벨테스트할때 주로 쓰고 되도록이면 지양하는게 좋다

### CSS상속(MDN에서 확인해보기-웹검색시 이용)

- 상속을 통해 부모 요소의 속성을 자식에게 상속한다(모두는 아님)
- 상속 되는 것은 폰트, 컬러, 텍스트 정렬
- 상속되지 않는 것 boxmodel관련, position관련 요소 등
- 

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    p {
      color: red; #색은 상속받음
      border: 1px solid black; #테두리는 김싸피가 상속받지 못함
    }
    span {
      border: 1px solid black; #따로 지정해주면 적용됨
    }

  </style>
</head>
<body>
  <p>안녕하세요. <span>김싸피</span>입니다.</p>
</body>
</html>
```

### (상대)크기 단위

- px(픽셀)
- %
- em
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- rem
  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .em {
      font-size: 1.5em;
    }
    .rem {
      font-size: 1.5rem; 
    }
  </style>
  
</head>
<body>
  <ul class="em"> 
    <li class="em">em</li>
    <li class="rem">rem</li>
    <li>no class</li>
  </ul>
</body>
</html>
```

- `.em`, `.rem` : 둘다 사이즈를 같게 설정했지만 실제 출력값은 다름
- 위코드 `.em`
  - 이게 실제 폰트가 36px(`16*1.5*1,5(부모사이즈)`)로 뜸 html의 기본 폰트는 16px이다
  - 부모에 사이즈가 em으로 설정되어 있음, em을 쓰면 고정이 안될 수 있음 rem을 쓰면 내가 원하는 값 나옴 em은 부모와 상대적 크기비교 때 사용
- 위코드 `.rem`
  - 이건 24px(16pxX1.5)

### 색상 단위

- 색상 키워드
- RGB 색상
  - '#' + 16진수 표기법
  - rgb() 함수형 표기법
- HSL 색상

### CSS 문서 표현

- 텍스트
  - 변형 서체
- 컬러, 배경(background-image, background-color)
  - 이미지는 디자인뿐만아니라 컨텐츠와 연관이 있는 경우
  - 배경 background-image는 단순 다자인요소이 일 때 사용, 또는 이미지 위에 글씨를 작성할 때 사용
- 목록 꾸미기

## Box model

- 개발자모드에 computed 탭에서 볼 수 있음
- CSS는 네모 세상 동그라미도 네모를 깎은 거다
- Margin
  - 테두리 바깥의 외부 여백 배경색을 지정할 수 없다
- Border
  - 테두리 영역
- Padding
  - 테두리 안쪽의 내부 여백, 요소에 적용된 배경색 이미지는 padding까지 적용
  - 보더와 컨텐트 사이
- Content
  - 글이나 이미지 등 요소 실제 내용

### Box model 구성(margin/padding)

- 상하좌우

```
.margin-1{
margin:10px;
}
```

- 상하/좌우

```
.margin-2{
margin:10px 20px;
}
```

- 상/좌우/하

```
.margin-3{
margin:10px 20px 30px;
}
```

- 상/우/하/좌

```
.margin-4{
margin:10px 20px 30px 40px;
}
```

- 위쪽에 마진값을준다->아래로 움직인다
- 가운데 정렬
  - 상하는 0(0값은 단위를 굳이 안붙임) 좌우는 auto(자동맞춤)

```
<head>
  <style>
    .bowl {
      width: 500px;
      border-width: 2px;
      border-style: dashed;
      border-color: black;
      margin-top: 10px ;
      margin-bottom: 30px; 
    }
    .box2 {
      width: 500px;
      border: 2px solid red;
      margin: 0 auto; 
    }
  </style>
</head>
```

### box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box
  - padding을 제외한 순수 contents영역만들 box로 설정
- 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함
  - 그 경우 box-sizing을 border-box으로 설정
- 보통 CSS최상단에서 보더박스를 전체선택자(`*`)로 다 적용해주고 시작

```
  <style>
    .box {
      width: 100px;
      margin: 10px auto;
      padding: 20px;
      border: 1px solid black;
      background-color: blueviolet;
      color: white;
      text-align: center;
    }
    .box-sizing {
      box-sizing: border-box;
    }
  </style>
```

### DIsplay

- display : block
  - 줄바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지함
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
  - ex) div / ul, ol, li/ p/ hr/ form 등
- display : inline
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지함
  - width, height, nargin-top, margin-bottom을 지정할 수 없다.
  - 상하 여백은 line-height로 지정
  - ex) span / a / img / input, label / b , em, i, strong 등

| 속성에 따른 수평 정렬 | block                               | inline             |
| --------------------- | ----------------------------------- | ------------------ |
| 왼쪽 정렬             | margin-right:auto;                  | text-align:left;   |
| 오른쪽 정렬           | margin-left:auto;                   | text-align:right;  |
| 가운데 정렬           | margin-right:auto;margin-left:auto; | text-align:center; |

## CSS Position (중요)

- 문서 상에서 요소를 배치하는 방법을 지정

- `static` 디폴트 값(기준 위치)

- 기본적인 요소의 배치 순서에 따름(좌측 상단)

  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치

- 아래는 좌표 프로퍼티(`top`, `bottom`, `left`, `right`)를 사용하여 이동이 가능(음수 값도 가능)

- ```
  relative
  ```

   

  :

   

  ```
  static 위치
  ```

  를 기준으로 이동(상대 위치)

  - 설정된 조상의 position이 default값(=static으로 설정됨)이라면.

- ```
  absolute
  ```

   

  : static이 아닌

   

  ```
  가장 가까이 있는 부모/조상 요소
  ```

  를 기준으로 이동(절대위치)

  - 설정된 조상의 position이 default값(=static으로 설정됨)이 아니라면 바로 위 조상을 기준으로!

- ```
  fixed
  ```

   

  : 부모 요소와 관계 없이

   

  ```
  브라우저를 기준
  ```

  으로 이동(교정 위치)

  - 스크롤시에도 항상 같은 곳에 위치

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    div {
      box-sizing: border-box;
      width: 100px;
      height: 100px;
      text-align: center;
      line-height: 100px;
      border: 1px solid black;
    }

    .parent {
      position: relative;
      width: 300px;
      height: 300px;
    }

    .sibling {
      width: 200px;
      height: 100px;
      background-color: deepskyblue;
    }

    .absolute {
      position: absolute;
      background-color: crimson;
      top: 100px;
    }

    .relative {
      position: relative;
      background-color: crimson;
      top: 100px;
    }

  </style>
</head>
<body>
  <div class="parent">
    <div class="absolute">형</div>
    <div class="sibling">동생</div>
  </div>
  <div class="parent">
    <div class="relative">형</div>
    <div class="sibling">동생</div>
  </div>
</body>
</html>
```

## css layout

CSS Layout

웹페이지에 포함되는 요소들을 어떻게 취합하고 그것들이 어느 위치에 놓일 것인지를 제어한다.


float

한 요소(element)가 정상 흐름(normal flow)으로부터 빠져 텍스트 및 인라인(inline) 요소가 그 주위를 감싸 자기 컨테이너의 좌,우측을 따라 배치되어야 함을 지정한다.

clearfix


float 요소와 다른 텍스트가아닌 block 요소간의 레이아웃 깨짐을 막기 위해 다음과 같이 작성한다.
/* float 속성을 적용한 요소의 부모요소에 적용한다. */
/* 부모 태그 다음에 가상 요소(::after)로 내용이 빈(content:"") 블럭(display: block;)을 만들고 */
/* 이 가상요소는 float left,right(both)를 초기화 한다는 뜻 */

.clearfix::after {
  content: "";
  display: block;
  clear: both;
}


정리

flexbox 및 그리드 레이아웃과 같은 기술이 나오기 이전에 float는 열 레이아웃을 만드는데 사용되었다.
mdn에서는 더 새롭고 나은 레이아웃 기술이 나와있으므로 레거시 레이아웃 기술로 분류해놓기도 했다.
결국 원래 텍스트 블록 내에서 float 이미지를 위한 역할로 돌아간 것이다.
여전히 사용하는 경우도 있다. (ex. naver nav bar)



flexbox

일명 flexbox라 불리는 Flexible Box module은 flexbox 인터페이스 내의 아이템 간 공간 배분과 강력한 정렬 기능을 제공하기 위한 1차원 레이아웃 모델로 설계되었다.
웹페이지의 컨테이너에 아이템의 폭과 높이 또는 순서를 변경해서 웹페이지의 사용 가능한 공간을 최대한 채우고 이를 디바이스 종류에 따라 유연하게 반영하도록 하는 개념


핵심 개념

요소

flex container
flex items


축

maix axis (주축)
cros axis (교차축)



flex container

flexbox 레이아웃을 형성하는 가장 기본적인 모델
flexbox가 놓여있는 영역
flex 컨테이너를 생성하려면 영역 내의 컨테이너 요소의 display 값을 flex 혹은 inline-flex로 지정
flex 컨테이너를 선언시 아래와 같이 기본 값이 지정

item은 행으로 나열
item은 주축의 시작 선에서 시작
item은 교차축의 크기를 채우기 위해 늘어남

flex-wrap 속성은 nowrap으로 지정



Tip !

justify - main axis
align - cross axis

content - 여러 줄
items - 한 줄
self - 개별 요소
flex-direction

쌓이는 방향 설정 (main-axis 의 방향만 바뀜. flex 는 single-direction layout concept 이기 때문)


row (기본값)

가로로 요소가 쌓임
row 는 주축의 방향을 왼쪽에서 오른쪽으로 흐르게 한다.


row-reverse
column

세로로 요소가 쌓임
column 은 주축의 방향을 위에서 아래로 흐르게 한다.


column-reverse

flex-wrap

item들이 강제로 한 줄에 배치 되게 할 것인지 여부 설정


nowrap (기본 값)

모든 아이템들 한 줄에 나타내려고 함 (그래서 자리가 없어도 튀어나옴)


wrap : 넘치면 그 다음 줄로
wrap-reverse : 넘치면 그 윗줄로 (역순)

flex-flow

flex-direction 과 flex-wrap 의 shorthand

flex-flow: row nowrap;
justify-content

main axis 정렬
flex-direction: row 기준으로 작성됨


flex-start (기본 값)

시작 지점에서 쌓임(왼쪽 → 오른쪽)


flex-end

쌓이는 방향이 반대 (flex-direction: row-reverse 와는 다르다. 아이템의 순서는 그대로 정렬만 우측에 되는 것.)


center
space-between

좌우 정렬 (item 들 간격 동일)


space-around

균등 좌우 정렬 (내부 요소 여백은 외곽 여백의 2배)


space-evenly

균등 정렬 (내부 요소 여백과 외각 여백 모두 동일)



align-items

cross axis 여러 줄 정렬
flex-direction: row 기준으로 작성됨


stretch (기본 값)

컨테이너를 가득 채움


flex-start

위


flex-end

아래


center
baseline

item 내부의 text에 기준선을 맞춤



align-self

align-items 와 동일 (단, 개별 item 에 적용)


auto (기본 값)
flex-start
flex-end
center
baseline
stretch

부모 컨테이너에 자동으로 맞춰서 늘어난다. (Stretch 'auto'-sized items to fit the container)



order

기본 값 : 0
작은 숫자 일수록 앞(왼쪽)으로 이동.

flex-grow

기본 값 : 0
주축에서 남는 공간을 항목들에게 분배하는 방법
각 아이템의 상대적 비율을 정하는 것이 아님
음수는 불가능



Bootstrap

The most popular HTML, CSS, and JS library in the world.



트위터에서 시작된 오픈 소스 프론트엔드 라이브러리


웹 페이지에서 많이 쓰이는 요소를 거의 전부 내장하고 있다.


디자인을 할 시간이 크게 줄어들고, 여러 웹 브라우저를 지원하기 위한 크로스 브라우징에 골머리를 썩일 필요가 없다.


웹 브라우저 크기에 따라 자동으로 정렬되는 "그리드 시스템"을 지원하며,


"one souce multi use" → 반응형 웹 디자인을 추구한다.


Responsive web design

layout은 방문자의 화면 해상도를 고려하여야 한다.
스마트폰이나 태블릿 등 모바일 기기는 화면이 작기 때문에 가독성에 더욱 신경써야 한다.
보통 웹사이트가 축소되어 가로 스크롤 없이 콘텐츠를 볼 수 있으나 글자가 너무 작아지기 때문이다.
데스크탑용, 테블릿용, 모바일용 웹사이트를 별도 구축할 수도 있지만 One Source Multi Use의 관점에서 올바른 해결책은 아니다.
반응형 웹 디자인(Responsive Web Design)은 화면 해상도에 따라 가로폭이나 배치를 변경하여 가독성을 높여 이러한 문제를 해결한다.
즉, 하나의 웹사이트를 구축하여 다양한 디바이스의 화면 해상도에 최적화된 웹사이트를 제공하는 것이다.



Bootstrap Grid System
Grid System

부트스트랩의 grid system 은 containers, rows 그리고 columns 를 사용해서 컨텐츠를 레이아웃하고 정렬한다.
모바일 우선 flexbox grid 를 사용하여 12개의 column 시스템을 가지고 있다.
왜 12 columns 일까 ?

12는 약수가 가장 많기 때문에 한 줄에 표시할 수 있는 종류가 제일 많다.


다음과 같은 구조로 사용한다.

.container > .row > col-*



.row

row 는 columns 의 wrapper 이다.
각 column 에는 공간 사이를 제어하기 위한 좌우 padding 값이 있는데 이를 gutter 라고도 한다.

row 의 margin 값과 gutter 를 제거하려면 .row 에 .no-gutters class 를 사용한다.



.col /  .col-*

column class 는 row 당 가능한 12개 중 사용하려는 columns 수를 나타낸다.
columns 너비는 백분율로 설정 되므로 항상 부모 요소를 기준으로 유동적으로 크기가 조정된다.
grid layout 에서 내용은 반드시 columns 안에 있어야 하며 그리고 오직 columns 만 row 의 바로 하위 자식 일 수 있다.

offset


offset-* 은 지정한 만큼의 column 공간을 무시하고 다음 공간부터 컨텐츠를 적용한다.

Nesting

.row > .col-* > .row > .col-* 의 방식으로 중첩 사용 가능하다.

Grid breakpoints

부트스트랩 grid system 은 다양한 디바이스에서 적용하기 위해 특정 px 조건에 대한 지점을 정해 두었는데 이를 breakpoints 라고 한다.
부트스트랩은 대부분의 크기를 정의하기 위해 em 또는 rem 을 사용하지만 px 는 그리드  breakpoint 에 사용된다. (뷰포트 너비가 픽셀 단위이고 글꼴 크기에 따라 변하지 않기 때문)



마무리

각각의 기술은 저마다 용도가 있고, 장단점이 있으며, 독립적인 용도를 갖추도록 설계된 기술은 없다.
특정 상황에 어떤 기술이 가장 적합한 도구가 될 것인지 파악하는 데에는 많은 경험이 필요하다.

RESET CSS

모든 HTML 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축된 규칙 세트
HTML5 Element, Typograph, Table, List 등의 요소들에 일관성있게 스타일을 적용 시키는 기본 단계


사용 배경

모든 브라우저는 각자의 user agent stylesheet 를 가지고 있는데 (웹사이트를 보다 읽기 편하게 하기 위해)
문제는 이 설정이 브라우저마다 상이하다는 것


종류
Normalize CSS

gentle solution


W3C 의 표준을 기준으로 브라우저 중 하나가 불일치 한다면 차이가 있는 브라우저를 수정한다.
경우에 따라 IE 또는 EDGE 는 표준에 따라 수정할 수 없는 경우도 있는데, 이 경우 Normalize 는 IE 또는 EDGE 의 스타일을 나머지 브라우저에 적용시킨다.
실제 bootstrap 에서는 normalize.css를 자체적으로 커스텀해서 bootstrap-reboot.css 라는 이름으로 사용한다.

Reset CSS

aggressive solution


브라우저의 기본 스타일이 전혀 필요 없다는 방식으로 접근한다.
따라서 브라우저의 user agent와 함께 제공되는 모든 스타일을 재설정한다.
Reset CSS의 문제점은 너무나 많은 선택자가 엉켜있고, 불필요한 오버라이드가 많이 발생하며 디버깅 시 제대로 읽을 수 없다.


마무리

현재는 Normalize CSS 를 중심으로 사용하고 여기에 적절한 Reset CSS 을 섞어 쓰라고 권장한다. (오래된 Reset CSS 를 사용하지 않도록 주의한다.)
무엇보다 더 중요한 건, "내 프로젝트에 명확하게 필요한 사항들인지 확인"

최종적으로 자신만의 Reset style sheet를 만들어 나가기는 것이 좋다.