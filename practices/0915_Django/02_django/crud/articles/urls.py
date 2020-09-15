from django.urls import path,include
from . import views
app_name = 'articles'
urlpatterns = [
    path('',views.read, name = 'read'),
    path('create/', views.create, name = 'create'),
    path('<int:article_pk>/', views.detail, name = 'detail'),
]
