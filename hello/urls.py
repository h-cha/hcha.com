import django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='test'),
    #path('work1', views.work1, name='work1'),
    #path('work2', views.work1, name='work2'),
    #path('work3', views.work1, name='work3'),
    #path('work4', views.work1, name='work4'),
]
