from django.urls import path
from . import views
app_name = 'community'
urlpatterns = [
    path('',views.review_list, name = 'review_list'),
    path('create/',views.create, name = 'create'),
    path('<int:review_pk>/',views.review_detail, name = 'review_detail'),
    path('<int:review_pk>/update/',views.review_update, name = 'review_update'),
    path('<int:review_pk>/delete/',views.review_delete, name = 'review_delete'),
]
