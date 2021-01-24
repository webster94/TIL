from django.urls import path
from . import views

app_name = 'articles' # 같은 변수중복을 막기위해 구분을 하나 만들어줌
urlpatterns = [  # url들의 집합소
    path('',views.index, name='index'),
    path('new/',views.new, name='new'),
    path('create/', views.create, name='create'),
     # 경로를 쉽게 정하기 위해서 name을 정했지
    # path서 비어 놓은 이유는 url의 가장 기본 페이지로 설정하기위해.
    path('<int:article_pk>/', views.detail, name='detail'),
]
