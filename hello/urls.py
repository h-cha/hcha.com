from django.urls import path
from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.index, name='index'),
    path('work1', views.work1, name='work1'),
    #path('work2', views.work1, name='work2'),
    #path('work3', views.work1, name='work3'),
    #path('work4', views.work1, name='work4'),
]
