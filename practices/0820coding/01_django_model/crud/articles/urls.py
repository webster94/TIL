from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [ 
    path('', views.index, name = 'index'),
    path('new/', views.new, name = 'new'), # throw - new에서 보내는 정보
    path('create/', views.create, name = 'create'),   # - new 에서보낸 정보
    # 받은 정보를 db저장
    path('<int:article_pk>/', views.detail, name = 'detail'),
    path('delete/<int:article_pk>/',views.delete, name = 'delete'),
    path('update/<int:article_pk>/',views.update, name = 'update'),
    path('modify/<int:article_pk>/',views.modify, name = 'modify'),
]