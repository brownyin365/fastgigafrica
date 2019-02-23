from django.urls import path
from . import views

app_name = 'digitalmarket'

urlpatterns = [
    path('create/', views.post_create, name='create'),
    path('list/', views.post_list, name='list'),
    path('detail/', views.post_detail, name='detail'),
    path('confirm/', views.post_confirm, name='confirm'),
    path('review/', views.post_review, name='review'),
    
]
