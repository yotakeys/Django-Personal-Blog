from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('post/<str:title>',views.post, name='post'),
]