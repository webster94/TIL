# Django Form

>  2020-09-14

사용자로부터 데이터를 받고 다시 검증하는 작업들을 Form을 통해 한다.



Form 은 django 프로젝트의 주요 유효성 검사 도구들 중 하나이며, 공격 및 우연한 데이터 손상에 대한 중요한 방어수단



django는 Form에 관련된 작업의 아래 세 부분을 처리

1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성
3. 클라이언트로부터 받은 데이터 수신 및 처리





Form class

1. django Form 관리 시스템의 핵심
2. form 내 field,field배치, 디스플레이, widget, label, 초기값, 유효하지 않은 field 에 관련된 에러메세지를 결정
3. django는 사용자의 데이터를 받을 때 해야할 과중한 작업(데이터 유효성 검증, 필요시 입력된 데이터 검증 결과 재출력, 유효한 데이터에 대해 요구되는 동작 수행 등)과 반복 코드를 줄여줌

오늘은 form class를 ,..놓쳐부려따





---

우리의 송쌤 강의

WEB을 통해 무언가를 만든다.

python , javascipt,html, css, django, vue!

회사에 취업을 했을 때., 회사가 다른 언어를 사용 할 수 있다.

대기업일수록 프레임워크들을 새로 만들 확률이 높다.

6개월 동안 배운 이 언어들에서 찾아보면 학습했던 공부방법을 통해 다른 언어사용시에 스스로 찾아보며 연결할 수 있게 된다. 

이러한 언어를 사용해서 각자의 목표를 구현하는 것이다.



전체 흐름!

서버,db, 크롬 익스텐션 - 검색자료임.

개발자는 공부를 피할 수 없다.



혼자서 도전해보는 것

여러분들이 만들 수 있는 것을 직접 만들어보는 것.

수업자료를 그대로 따라하는 것과 에러 - 이녀석을 어떻게 해결할 수 있을까? - 반드시 고민!

코더가 되지말자!

검색의 범위 또한 줄어들고, 질문 또한 명확!



---

오늘 하는 것

게시판을 갖고 있는 웹사이트를 만들 것이다.

글(article)

이 웹사이트는 글쓰기페이지와 상세페이지를 가고 있다.

메인페이지 - 글 리스트

글쓰기 - 글 쓸수 있는

상세페이지 - 글 상세정보

데이터베이스 - 글 정보가 저장될 공간

화면 - 페이지를 보여줄 화면

view url form template

뭘 통해서 이걸 만들까?

django 

---



1. 파일에서 crud생성

   django-admin startproject crud

2. 가상환경 생성 (venv)

   python -m venv venv

4. ctr + shift + p 누르고 select interpreter

5. pip install django >> pip freeze로 확인 4개 다운됨

6. python manage.py startapp article

   ```
   startproject
   startapp
   app 등록
   url - 어떤 페이지를 보여줄 건지? 
   view
    - model
    - view
   template
   ```

```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles'))
]

```

![image-20200914131802245](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200914131802245.png)

>  www. binsan.com/articles/delete << 다 붙여준다

![image-20200914132042458](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200914132042458.png)

 = www.binsan.com/article/이다.

name을 왜줬지?

app_name을 왜줬지?

---

![image-20200914141737427](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200914141737427.png)

>  이해하자

POST는 데이터를 받는 곳이므로, 정보를 일단 받아야한다.

POST가 아닌 경우

템플릿을 사용자에게 보여줘야하는 경우

form - ArticleForm()

context

return .... 아래것을 완성 한 후

위에 pass를 작성한다.





![image-20200914142245967](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200914142245967.png)

form 일 때는 유효성 검증하고나서도 필드별로 .get으로 저장해야한다

우리는 model.form을 통해 위에 처럼 적어줄 필요가없다.

model form이 갖고있기 때문에!

바로 form.save를 할 수 있다!





위젯 작성 2가지 방법

meta 태그 , class 바로아해! 후위 권장



뷰 데코레이터  = get, post만 받기위해 사용한다.

템플릿 밖에 저장 할떄 세팅에 필요한 단어

'DIRS': [BASE_DIR / 'templates'],

  'DIRS': [BASE_DIR / 'templates'],

​    \#"~~~~~/crud/templates"

​    \# crud는 최상위 폴더 BASE_DIR은 최상위폴더를 가르키고 있다.



![image-20200914165431303](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200914165431303.png)

> 글쓰기는 두가지 녀석이 둘다 필요하다.

def create(request):

  return render(request, 'articles/create.html')

  \# 글을 쓸수 있는 페이지를 보여주는 녀석임

```
from django.urls import path
from . import views # 가져온다

app_name = 'articles'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('create/',views.create, name = 'create'),
]
```

> url

```
from django.shortcuts import render , redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        "articles" : articles, 
    }
    return render(request, 'articles/index.html', context) 
    # template 이름
    # tmeplate를 가지고 render를 할건데 실제 html파일을 만드는 작업임
    # 템플릿을 기반으로 html을 만들고 사용자에게 보내준다는 로직임.

def create(request):
    if request.method == 'POST':
        # 글을 쓰는 로직!
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article()
        article.title = title
        article.content = content
        article.save()
        return redirect('articles:index')

    else: 
        return render(request, 'articles/create.html')
    # 글을 쓸수 있는 페이지를 보여주는 녀석임

```

> view

```
{% extends 'base.html' %}
{% block content %}
<a href="{% url 'articles:create' %}">새글쓰기</a>
<hr>
{% for article in articles %}
    <h1> {{article.title}}</h1>
    <p> {{article.content}}</p>
    <hr>
{% endfor %}
{% endblock content %}


<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD</title>
</head>
<body>
    {% block content %}

    {% endblock  %}
 # 구멍을 뚫는다
</body>
</html>
```

> templates

---

cr 까지 받았다...

마지막 마무리는

$ pip freeze > requirments.txt

를 꼭해줘야한다

.gitignore를 만들어서 파일을 제거해준다.

venv/

.vscode/

db.sqlite3





---

### 1.1 Django의 주요 특징 및 성격

- 주요 특징 : `Versatile` (다용도의), `Secure` (안전한), `Scalabe` (확장성 있는) , `Complete` (완결성 있는), `Maintainable` (쉬운 유지보수), `Portable` (포터블한 - 다양한 운영체제에서 작동 가능)

- django의 성격 : `다소 독선적` 이라고 공식 문서에서 명시됨

  - ```
    Opinionated
    ```

     

    (독선적) : 특정 프레임워크에 맞는 규칙(약속)을 반드시 지켜야 함

    - 개발의 자유도는 떨어지거나 유연한 개발이 어렵다.
    - 하지만 개발자가 손 볼 것이 많지 않다.
    - 최근에는 생산성이 높아야 하므로 `Opinionated` 이 대세다.

  - ```
    Unopinionated
    ```

     

    (관용적)

    - 자유도가 비교적 높아 제약이 거의 없이 여러 컴포넌트들을 붙여 사용할 수 있다.



### 1.2 가상 환경

#### (1)가상 환경을 사용하는 이유

- `의존성` 문제 : 본인의 컴퓨터에서 자 작동하던 프로그램도 다른 프로그램에 설치 했을 때 잘 동작하리라는 보장이 없음.
  - Python도 같은 버전, 같은 모듈을 쓴다는 보장이 없다.
- 특정 프로그램만을 실행하기 위한 Python 환경을 따로 만들어서 그 환경속에서만 모듈을 관리하고 앱을 실행하기 위해 가상환경을 설정한다.
  - 다른 앱을 실행시키는 일이 생기면 그 가상환경을 빠져나와 다른 환경을 만드는 방식으로 진행한다.
- `python -m venv` (가상환경 경로 + 이름)
  - `python -m venv ssafy` : 특정경로 없이 현재 위치에서 ssafy라는 이름의 가상환경이 만들어짐
  - `python -m venv ~/documents/ssafy`



#### (2) 가상 환경 만들기

- [1st]

   

  ```
  git bash
  ```

   

  명령어

  - `python -m venv venv` (이 과정만 수행하고 바로 `[2nd]`로 넘어가자)
  - `source venv/Scripts/activate`
  - `pip list` : update 명령어 실행
  - 다시 `pip list` 누르고 버전 확인
  - `deactivate` 가상환경 종료

- ⭐

   

  [2nd] `vscode` 에서 할 일 (이 과정은 vscode 켤 때마다 항상 실행할 과정 / 반드시 차례대로 수행!)

  - [Ctrl] + [Shift] + [P] 입력 후 `Python: Select Interpreter` 선택
  - `venv` 적힌 Python 버전 선택
  - 기존에 켜져 있는 `vscode`의 터미널 강제 종료 후 다시 터미널 실행한다.
  - 새로 열린 터미널에서 `(venv)` 적힌거 확인하고 `pip list`로 버전 및 가상환경 확인 (**반드시 가상환경을 먼저 켜고(상위 세 과정) 터미널을 열자!**)
  - update 명령어 나오면 항상 수행하자

> 만약 [Ctrl] + [`] 단축키 안 될 때(Option)

---

0915



- 데이터베이스 안 테이블 이름은 앱 이름과 모델 안 클래스이름이 들어가게된다.
  - ex ) articles_article
- post 통과
- post 통과



---

이미지 설정법

이미미

 model 등록

pip install pillow 



views.py 에서 

form 에 files = request.FILE

create.py 에서 enctype 추가

내가 원하는 위치에 저장이 안되서 문제임

따로 폴더를 만들어서 관리를 하고싶다.

설정을해야할 것은 

setting에 저장



media에 저장이되면 읽어와야하는데

url설정을 해줘야함

static에 설정을 햇음





---

Cookeie % Session 

![image-20200916104724653](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200916104724653.png)

> Cookie 와 session 을 알기 전에 HTTP의 속성에 대해 알고 들어가보자

> 봐야할 특징 : 비연결지향, 무상태
>
> 계속 로그인을 유지시켜주기 위해 존재하는 것이 쿠키와 세션



![image-20200916105115451](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200916105115451.png)

재밌넹



쿠키는  로컬에 저장

서버는 세션을 지운다.

![image-20200916110008607](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200916110008607.png)

> 클라이언트는 session id를 쿠키에 저장시킨다.

![image-20200916110638638](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200916110638638.png)

> 흐름도 (좌측이 클라이언트), (우측이 서버)

클라이언트(브라우저가 대신 함) : 서버로 부터 정보를 받는 컴퓨터



서버는 클라이언트에게 네트워크를 통해 정보나 서비스를 제공하는 컴퓨터 시스템

서버는 응답을 주고 클라이언트는 응답을 받는다.

세션은 중요한 내용임



![image-20200916111219759](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200916111219759.png)

![image-20200916111352159](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200916111352159.png)

> sign up  = user create
>
> login session create!

---

# 송쌤 0916

> form vs modelForm의 차이

form

- model과 밀접한 관계가 없을 때 폼을 사용
- modelForm은 밀접한 관계가 있을 때 폼을 사용

django user

회원가입할 때는 user model UserCreationFrom- moddelForm사용

이메일, 아이디, 비밀번호, 주소, 이름

로그인은 아이디와 비밀번호만 필요하다.

장고가 판단하기에 밀접한 관계가 아닌 것을 표기

그래서 AuthenticationForm -form을 사용!

```
from django.shortcuts import render,redirect
# Create your views here.
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
if request.method == 'POST':
    form = ArticleForm(request.POST) 
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
else:
    form = ArticleForm()
context = {
    'form': form,
}
return render(request, 'articles/create.html', context)

def detail(request, pk):
article = Article.objects.get(pk=pk)
context = {
    'article': article,
}
return render(request, 'articles/detail.html', context)

def update(request, pk):
article = Article.objects.get(pk=pk)
if request.method == 'POST':
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
else:
    form = ArticleForm(instance=article)
context = {
    'form': form,
    'article': article,
}
return render(request, 'articles/update.html', context)

def delete(request, pk):
if request.user.is_authenticated:
    article = Article.objects.get(pk=pk)
    article.delete()
return redirect('articles:index')
```

```
from django.urls import path
from . import views
app_name = 'articles'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]

```





```
form을 잘모르겟넹 
복붙함 

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
 
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name','last_name')


```

---

왜 비밀번호는

![image-20200917114037286](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200917114037286.png)

해시로 저장되는가?

>
>
>모든 서버는 password자체를 그대로 저장하지않는다.
>
>password를 내가 그대로 저장하면 무슨일이 일어날까?

1. 나(관리자) - db에 접속가능, 모든 데이터 확인 가능
2. 모든 유저의 아디와 비번 내가 get할 수 있음.
3. db가 털렸을 때, 모든 내 이용자의 password가 털리는 것

![image-20200917144226011](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200917144226011.png)



---



# 오창희 교수님

